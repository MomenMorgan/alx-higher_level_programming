#!/usr/bin/python3
import MySQLdb
import sys

"""script that takes in an argument and displays all values 
in the states table of hbtn_0e_0_usa where name matches the argument."""

if __name__ == "__main__":
        """Initialize connection"""
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
        """Create a cursor"""
        cur = db.cursor()
        """Executes query"""
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                        ORDER BY states.id ASC".format(sys.argv[4]))
        """Obtain all records"""
        rows = cur.fetchall()
        """Print all records"""
        for row in rows:
                print(row)
        """Close cursor"""
        cur.close()
        """Close connection"""
        db.close()
      