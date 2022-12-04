#!/usr/bin/python3
"""
lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], password=argv[2], databse=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in cursor.fetchall() if state[1][0] == "N"]
