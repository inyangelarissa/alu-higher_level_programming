#!/usr/bin/python3
"""
Secure script to filter states in a database
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Ensure proper usage
    if len(sys.argv) != 5:
        print("Usage: ./3-my_safe_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    # Retrieve command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to the database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        # Create a cursor object to execute queries
        cursor = db.cursor()

        # Secure query with parameterized input
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        # Fetch and print the results
        results = cursor.fetchall()
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        # Close the database connection
        if 'db' in locals() and db.open:
            db.close()

