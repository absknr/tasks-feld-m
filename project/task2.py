from datetime import datetime
from db import fetch_one

NUM_DAY_MAP = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


def run():
    sql = """
    SELECT t.datetime, max(t.revenue)
    FROM transactions t
    JOIN devices d ON d.id = t.device_type
    WHERE d.device_name = 'Mobile Phone'"""

    result = fetch_one(sql)

    if result:
        date_time, _ = result
        datetime_obj = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")

        print(
            "Day most revenue for users who ordered via a mobile phone: {} {}".format(
                NUM_DAY_MAP[datetime_obj.weekday()], datetime_obj.strftime("%Y-%m-%d")
            )
        )
    else:
        print("No visitors were found")


if __name__ == "__main__":
    run()
