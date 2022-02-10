from db import execute
from utils import abs_curdirfile_path

TXT_FILE_NAME = "task3.txt"


def append_new_line(str):
    return str + "\n"


def run():
    sql = """
    SELECT t.*, d.*
    FROM transactions t
    JOIN devices d
    ON d.id = t.device_type"""

    cur = execute(sql)

    file_path = abs_curdirfile_path(__file__, TXT_FILE_NAME)

    # clear a file before writing so that
    # records are not duplicated on script re-run.
    open(file_path, "w").close()

    with open(file_path, "a") as file:
        cols_name_gen = (desc[0] for desc in cur.description)
        first_line = append_new_line(",".join(cols_name_gen))
        file.write(first_line)

        for result in cur:
            cols_val_gen = (str(col_val) for col_val in result)
            line = append_new_line(",".join(cols_val_gen))
            file.write(line)

    print("Created {} successfully.".format(TXT_FILE_NAME))


if __name__ == "__main__":
    run()
