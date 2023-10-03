import csv
import requests
import sys

def fetch_employee_data(employee_id):
  """Fetches employee data from the JSONPlaceholder API.

  Args:
    employee_id: The ID of the employee to fetch data for.

  Returns:
    A dictionary containing the employee's data.
  """

  # Define the API endpoints
  user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
  todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

  try:
    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch TODO list data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    return user_data, todos_data

  except requests.exceptions.RequestException as e:
    print("Error: Unable to fetch data from the API.")
    print(e)

def export_employee_TODO_list_to_CSV(employee_data, todos_data):
  """Exports the employee's TODO list data to a CSV file.

  Args:
    employee_data: A dictionary containing the employee's data.
    todos_data: A list of dictionaries containing the employee's TODO list items.
  """

  # Create a new CSV file
  csv_file = open(f"{employee_data['id']}.csv", "w", newline="")

  # Create a CSV writer object
  csv_writer = csv.writer(csv_file)

  # Write the header row to the CSV file
  csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

  # Iterate over the employee's TODO list data and write each task to the CSV file
  for task in todos_data:
    csv_writer.writerow([
      employee_data["id"],
      employee_data["username"],
      task["completed"],
      task["title"],
    ])

  # Close the CSV file
  csv_file.close()

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python script.py <employee_id>")
  else:
    employee_id = int(sys.argv[1])

    user_data, todos_data = fetch_employee_data(employee_id)
    export_employee_TODO_list_to_CSV(user_data, todos_data)

