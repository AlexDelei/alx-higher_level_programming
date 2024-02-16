#!/usr/bin/python3
"""
Lets list everything in our new database
"""
import MySQLdb


db = MySQLdb.connect(user="root", password="root", database="hbtn_0e_0_usa")
all_items = db.cursor()
all_items.execute(
        "SELECT * FROM states "
        "ORDER BY states.id ASC"
        )
result = all_items.fetchall()


if __name__ == '__main__':
    for i in result:
        print(i)
