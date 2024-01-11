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

    cur.execute("SELECT * FROM states ORDER BY id")

    rows = cur.fetchall()
    for row in rows:
        print(row)
