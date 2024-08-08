#!/usr/bin/python3
"""Script to list all states from the database hbtn_0e_0_usa."""
import MySQLdb, sys; db=MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]); c=db.cursor(); c.execute("SELECT * FROM states ORDER BY id"); [print(row) for row in c.fetchall()]
if __name__ == "__main__": pass

