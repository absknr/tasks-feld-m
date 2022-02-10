from distutils.filelist import findall
import xml.etree.ElementTree as ET

from db import execute
from utils import abs_curdirfile_path


def data_gen(date_rate_map):
    sql = "select id, datetime from transactions"

    cur = execute(sql)

    for id, datetime in cur:
        date = datetime.split(" ")[0]

        if date not in date_rate_map:
            continue

        yield (date_rate_map[date], id)


def run():
    namespaces = {"ex": "http://www.ecb.int/vocabulary/2002-08-01/eurofxref"}

    tree = ET.parse(abs_curdirfile_path(__file__, "eurofxref-hist-90d.xml"))
    root = tree.getroot()

    date_rate_map = {
        cube_time.attrib["time"]: float(
            cube_time.find("./ex:Cube[@currency='USD']", namespaces=namespaces).get(
                "rate"
            )
        )
        for cube_time in root.findall(".//ex:Cube[@time]", namespaces=namespaces)
    }

    update_sql = "UPDATE transactions SET revenue = revenue / ? WHERE id = ?"

    execute(update_sql, params=data_gen(date_rate_map), exec_type="many")

    print("Records updated successfully.")


if __name__ == "__main__":
    run()
