import requests

def get_employee_todo_list_progress(employee_id):
  """Returns information about the employee's TODO list progress.

  Args:
    employee_id: The ID of the employee.

  Returns:
    A string containing the employee's TODO list progress in the format:

    Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    TASK_TITLE

    where:
    EMPLOYEE_NAME: name of the employee
    NUMBER_OF_DONE_TASKS: number of completed tasks
    TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
    TASK_TITLE: title of the completed task
  """

  # Get the employee's TODO list items.
  response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
  todo_list_items = response.json()

  # Get the employee's name.
  response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
  employee = response.json()
  employee_name = employee["name"]

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

  # Generate the output string.
  output_string = f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):\n"
  for todo_list_item in todo_list_items:
    if todo_list_item["completed"]:
      output_string += f"  {todo_list_item['title']}\n"

  return output_string


if __name__ == "__main__":
  # Get the employee ID from the user.
  employee_id = int(input("Enter the employee ID: "))

  # Get the employee's TODO list progress.
  employee_todo_list_progress = get_employee_todo_list_progress(employee_id)

  # Print the employee's TODO list progress to the console.
  print(employee_todo_list_progress)
