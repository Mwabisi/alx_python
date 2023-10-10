import MySQLdb
import sys

def list_cities_by_state(username, password, database_name, state_name):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )

        cursor = db.cursor()

        # Prepare the SQL query with parameterized query to avoid SQL injection
        query = """
        SELECT cities.id, cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """

        cursor.execute(query, (state_name,))

        rows = cursor.fetchall()

        # Extract city names and join them into a comma-separated string
        cities_list = [row[1] for row in rows]
        cities_str = ', '.join(cities_list)

        # Display the results as a comma-separated string
        print(cities_str)

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

    list_cities_by_state(username, password, database_name, state_name)
