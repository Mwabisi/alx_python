import MySQLdb
import sys


def list_states_with_name_starting_with_n(username, password, database_name):
  """
  Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.

  Args:
    username: The MySQL username.
    password: The MySQL password.
    database_name: The database name.

  Returns:
    A list of states with a name starting with N (upper N), sorted in ascending order by states.id.
  """

  # Connect to the MySQL server.
  db = MySQLdb.connect(
      host="localhost",
      port=3306,
      user=username,
      passwd=password,
      db=database_name,
  )

  # Create a cursor object to interact with the database.
  cursor = db.cursor()

  # Execute the SQL query to select states with names starting with 'N'.
  cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

  # Fetch all the matching rows.
  rows = cursor.fetchall()

  # Display the results.
  for row in rows:
    print(row)

  # Close the cursor and the database connection.
  cursor.close()
  db.close()


if __name__ == "__main__":
  if len(sys.argv) != 4:
    print("Usage: python script.py <username> <password> <database_name>")
    sys.exit(1)

  username = sys.argv[1]
  password = sys.argv[2]
  database_name = sys.argv[3]

  list_states_with_name_starting_with_n(username, password, database_name)
