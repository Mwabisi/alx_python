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

def display_employee_TODO_list_progress(user_data, todos_data):
  """Displays the employee's TODO list progress.

  Args:
    user_data: A dictionary containing the employee's data.
    todos_data: A list of dictionaries containing the employee's TODO list items.
  """

  # Calculate the number of completed tasks
  completed_tasks = [task for task in todos_data if task["completed"]]
  num_completed_tasks = len(completed_tasks)
  total_num_tasks = len(todos_data)

  # Display employee TODO list progress
  print(f"Employee {user_data['name']} is done with tasks({num_completed_tasks}/{total_num_tasks}):")
  for task in completed_tasks:
    # Check task formatting
    if not task["title"].strip().endswith('.'):
      task["title"] += '.'

    print(f"\t{task['title']}")

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python script.py <employee_id>")
  else:
    employee_id = int(sys.argv[1])

    user_data, todos_data = fetch_employee_data(employee_id)
    display_employee_TODO_list_progress(user_data, todos_data)
