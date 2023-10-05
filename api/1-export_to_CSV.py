"""
This module gathers and prints information about the task completion status of an employee.
The employee data is obtained from an API endpoint.
"""

import requests
import sys
import csv

def get_employee_data(employee_id):
    """
    Fetches data about the employee and their tasks from an API.

    Args:
    employee_id (int): The ID of the employee.

    Returns:
    dict: The information about the employee.
    dict: The tasks of the employee.
    """
    
    user_info = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}').json()
    todos = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos').json()
    
    return user_info, todos

def write_to_csv(user_info, todos):
    """
    Writes the tasks of an employee to a CSV file.

    Args:
    user_info (dict): The information about the employee.
    todos (dict): The tasks of the employee.
    """
    
    filename = f"{user_info.get('id')}.csv"
    with open(filename, 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        taskwriter.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos:
            taskwriter.writerow([user_info.get('id'), user_info.get('username'), task.get('completed'), task.get('title')])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
    else:
        user_info, todos = get_employee_data(sys.argv[1])
        write_to_csv(user_info, todos)