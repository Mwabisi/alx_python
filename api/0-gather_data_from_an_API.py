import json
import requests

def get_employee_todo_list_progress(employee_id):
  """Gets the TODO list progress for an employee with the given employee ID.

  Args:
    employee_id: The employee ID.

  Returns:
    A dictionary containing the following information about the employee's TODO
    list progress:
      * name: The employee's name.
      * number_of_done_tasks: The number of completed tasks.
      * total_number_of_tasks: The total number of tasks.
      * completed_tasks: A list of the titles of the completed tasks.
  """

  # Get the employee's TODO list items.
  todo_list_items_endpoint = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
  todo_list_items_response = requests.get(todo_list_items_endpoint)
  todo_list_items = json.loads(todo_list_items_response.content)

  # Get the employee's name.
  employee_details_endpoint = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
  employee_details_response = requests.get(employee_details_endpoint)
  employee_details = json.loads(employee_details_response.content)
  employee_name = employee_details["name"]

  # Calculate the number of completed and non-completed tasks.
  number_of_done_tasks = 0
  number_of_non_completed_tasks = 0
  for todo_list_item in todo_list_items:
    if todo_list_item["completed"]:
      number_of_done_tasks += 1
    else:
      number_of_non_completed_tasks += 1

  # Calculate the total number of tasks.
  total_number_of_tasks = number_of_done_tasks + number_of_non_completed_tasks

  # Get the titles of the completed tasks.
  completed_tasks = []
  for todo_list_item in todo_list_items:
    if todo_list_item["completed"]:
      completed_tasks.append(todo_list_item["title"])

  # Return a dictionary containing the employee's TODO list progress.
  return {
    "name": employee_name,
    "number_of_done_tasks": number_of_done_tasks,
    "total_number_of_tasks": total_number_of_tasks,
    "completed_tasks": completed_tasks
  }


def main():
  # Get the employee ID from the user.
  employee_id = int(input("Enter the employee ID: "))

  # Get the employee's TODO list progress.
  employee_todo_list_progress = get_employee_todo_list_progress(employee_id)

  # Display the employee's TODO list progress on the standard output.
  print(f"Employee {employee_todo_list_progress['name']} is done with tasks({employee_todo_list_progress['number_of_done_tasks']}/{employee_todo_list_progress['total_number_of_tasks']}):")
  for completed_task in employee_todo_list_progress["completed_tasks"]:
    print(f"     {completed_task}")


if __name__ == "__main__":
  main()
