import sys
import sqlite3
import psycopg2

from configparser import ConfigParser
from utils import abs_curdirfile_path

CON = {}

SQLITE_DBFILE_PATH = abs_curdirfile_path(__file__, "transactions.db")

CONFIG_PARSER = ConfigParser()

# NOTE: Ideally, we can use a separate config file for each environment.
# Eg. File "db.prod.ini" for production related configs.
# However, environment resolution is omitted here for simplicity.
CONFIG_PARSER.read(abs_curdirfile_path(__file__, "db.ini"))


def get_con(db_type="sqlite"):
    """Fetches a DB connection. If an old connection is alive,
    it returns that connection otherwise it creates a new connection."""

    if not CON.get(db_type):
        if db_type == "postgres":
            config = {k: v for k, v in CONFIG_PARSER.items("postgresql")}
            CON["postgres"] = psycopg2.connect(**config)
        else:
            CON["sqlite"] = sqlite3.connect(SQLITE_DBFILE_PATH)

    return CON.get(db_type)


def exec_func(cur, exec_type=None):
    return cur.executemany if exec_type == "many" else cur.execute


def execute(sql, params=None, exec_type=None, db_type="sqlite"):
    """Executes a SQL query using an active connection and
    returns the Cursor object."""

    try:
        con = get_con(db_type)
        args = (sql, params) if params else (sql,)

        if db_type == "postgres":
            with con:
                cur = con.cursor()
                exec_func(cur, exec_type=exec_type)(*args)
                return cur

        cur = exec_func(con, exec_type=exec_type)(*args)
        con.commit()

        return cur

    except sqlite3.Error as e:
        print("An error occured:", e.args[0])
        sys.exit()


def fetch_all(*args, **kwargs):
    return execute(*args, **kwargs).fetchall()


def fetch_one(*args, **kwargs):
    return execute(*args, **kwargs).fetchone()


def close_con(db_type="sqlite"):
    if db_type == "postgres" and CON.get("postgres"):
        CON["postgres"].close()
    elif CON.get("sqlite"):
        CON["sqlite"].close()
