#!/usr/bin/python3
"""
listing according to science
"""
import MySQLdb
import sys


def list_caes(username, password, database):
    """"list view wothout restrications"""
    db = MySQLdb.connect(user=username, password=password, database=database)
    query = db.cursor()
    query.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' "
            "ORDER BY states.id ASC"
            )

    result = query.fetchall()

    for i in result:
        print(i)
    db.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: executable.py <username> <password> <database>")
        sys.exit(1)
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_caes(username, password, database)
