import MySQLdb
import sys

def search_states_by_name(username, password, database_name, search_name):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Prepare the SQL query with user input using format
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(search_name)

        # Execute the SQL query
        cursor.execute(query)

        # Fetch all the matching rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

        # Close the cursor and the database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database_name> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    search_states_by_name(username, password, database_name, state_name)
