import MySQLdb

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
  db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)

  # Create a cursor.
  cursor = db.cursor()

  # Execute the SQL query to list all states with a name starting with N (upper N).
  cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

  # Get the results.
  results = cursor.fetchall()

  # Close the cursor and the database connection.
  cursor.close()
  db.close()

  return results

# Get the MySQL username, password, and database name from the user.
username = input("Enter the MySQL username: ")
password = input("Enter the MySQL password: ")
database_name = input("Enter the database name: ")

# List all states with a name starting with N (upper N).
states = list_states_with_name_starting_with_n(username, password, database_name)

# Print the results.
print("List of states with a name starting with N:")
for state in states:
  print(state[1])
