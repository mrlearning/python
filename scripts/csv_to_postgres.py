#!/usr/bin/env python3

import sys
import requests
import psycopg2
from psycopg2 import sql


DATABASE_CONFIG = {
    "host": "192.168.167.94",
    "dbname": "test_db",
    "user": "postgres",
    "password": "postgres",
    "port": 5432
}

TABLE = "test"

CSV_SEPARATOR = ","


def fill_table(csv_url):
    conn = None
    sql_insert = sql.SQL("INSERT INTO {0}(id, date, url, count) VALUES(%s, %s, %s, %s)").format(sql.Identifier(TABLE))
    try:
        conn = psycopg2.connect(**DATABASE_CONFIG)
        cursor = conn.cursor()
        r = requests.get(csv_url, stream=True)
        for line in r.iter_lines():
            if line:
                decoded_line = line.decode("utf-8")
                values = decoded_line.split(CSV_SEPARATOR)
                cursor.execute(sql_insert, values)
        conn.commit()
    except psycopg2.DatabaseError as db_err:
        print(db_err)
    except BaseException as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Script takes exactly 1 argument. {0} given.".format(len(sys.argv)-1))
    else:
        fill_table(sys.argv[1])


