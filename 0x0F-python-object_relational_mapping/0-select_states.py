#!/usr/bin/python3
"""
 lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
	user=sys.argv[1],
	password=sys.argv[2],
	database=sys.argv[3],
	port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM state ORDER BY states.id")

    states = cursor.fetchall()

    for sate in states:
	print(state)

    cursor.close()
    db.close()
