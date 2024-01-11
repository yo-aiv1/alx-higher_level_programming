#!/usr/bin/python3
"""Retreave data from a database."""


if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
                        host="localhost",
                        user=sys.argv[1],
                        password=sys.argv[2],
                        db=sys.argv[3],
                        port=3306
                        )

    cur = db.cursor()
    arg = sys.argv[4]
    cur.execute("SELECT name FROM cities WHERE state_id = \
                (SELECT id FROM states WHERE name = %s)", (arg,))

    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
