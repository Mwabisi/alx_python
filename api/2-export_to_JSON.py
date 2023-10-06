"""
This module gathers and prints information about the task completion status of an employee.
The employee data is obtained from an API endpoint.
"""

import json
import requests
import sys

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

def write_to_json(user_info, todos):
    """
    Writes the tasks of an employee to a JSON file.

    Args:
    user_info (dict): The information about the employee.
    todos (dict): The tasks of the employee.
    """
    
    filename = f"{user_info.get('id')}.json"
    tasks = []
    for task in todos:
        tasks.append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': user_info.get('username')
        })
    with open(filename, 'w') as jsonfile:
        json.dump({user_info.get('id'): tasks}, jsonfile)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_JSON.py <employee_id>")
    else:
        user_info, todos = get_employee_data(sys.argv[1])
        write_to_json(user_info, todos)