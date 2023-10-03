import os

def export_employee_TODO_list_to_CSV(employee_data, todos_data):
  """Exports the employee's TODO list data to a CSV file.

  Args:
    employee_data: A dictionary containing the employee's data.
    todos_data: A list of dictionaries containing the employee's TODO list items.
  """

  # Create a new CSV file
  csv_file_path = f"{employee_data['id']}.csv"

  # Check if the CSV file exists
  if not os.path.exists(csv_file_path):
    # Create the CSV file
    with open(csv_file_path, "w", newline="") as csv_file:
      csv_writer = csv.writer(csv_file)

      # Write the header row to the CSV file
      csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

  # Write the employee's TODO list data to the CSV file
  with open(csv_file_path, "a", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)

    for task in todos_data:
      csv_writer.writerow([
        employee_data["id"],
        employee_data["username"],
        task["completed"],
        task["title"],
      ])

