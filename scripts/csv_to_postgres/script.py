#!/usr/bin/env python3

import argparse
import requests
import logging
import psycopg2
from psycopg2 import sql


DATABASE_CONFIG = {
    "host": "127.0.0.1",
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
        logging.error(db_err)
    except BaseException as e:
        logging.error(e)
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("csv_url", help="csv file url")
    args = arg_parser.parse_args()
    fill_table(args.csv_url)



