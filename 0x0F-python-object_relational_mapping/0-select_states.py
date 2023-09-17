#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':
    # The script takes 3 arguments: mysql username, mysql password and database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")

    # Getting a cursor in MySQLdb python
    cur = db.cursor()

    # Executing the Query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Obtaining the Query results
    query_rows = cur.fetchall()

    # Printing the rows obtained in the query
    for row in query_rows:
        print(row)

    # Close cursor
    cur.close()

    # Close connection
    db.close()
