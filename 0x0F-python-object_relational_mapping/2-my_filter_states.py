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

    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id", (arg,))

    rows = cur.fetchall()
    for row in rows:
        print(row)
