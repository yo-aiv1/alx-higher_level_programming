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

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states \
                ON cities.state_id = states.id ORDER BY states.id;")

    rows = cur.fetchall()
    for row in rows:
        print(row)
