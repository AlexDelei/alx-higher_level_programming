#!/usr/bin/python3
"""
Listing according to arguments
"""
import MySQLdb
import sys


def list_with_args(user, pwd, db, state):
    """
    params:
    -> username: the root user
    -> password: the root password
    -> database: hbtn_0e_0_usa
    -> state: the state to list from our db
    """
    db = MySQLdb.connect(
            user=user,
            password=pwd,
            database=db,
            host="localhost",
            port=3306)
    query = db.cursor()
    query.execute("SELECT * FROM states WHERE name = %s", (state,))

    result = query.fetchall()

    for i in result:
        print(i)
    db.close()


if __name__ == '__main__':
    # validates the arguments
    if len(sys.argv) != 5:
        print("Usage: exec.py <user> <passwd> <db> <state>")
        sys.exit(1)
    user, pwd, db, state = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    list_with_args(user, pwd, db, state)
