"""
This module gathers and prints information about the task completion status of an employee.
The employee data is obtained from an API endpoint.
"""

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

def print_employee_tasks(user_info, todos):
    """
    Prints the completed tasks of an employee.

    Args:
    user_info (dict): The information about the employee.
    todos (dict): The tasks of the employee.
    """
    
    completed_tasks = [task for task in todos if task.get('completed')]
    
    print(f"Employee {user_info.get('name')} is done with tasks({len(completed_tasks)}/{len(todos)}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        user_info, todos = get_employee_data(sys.argv[1])
        print_employee_tasks(user_info, todos)