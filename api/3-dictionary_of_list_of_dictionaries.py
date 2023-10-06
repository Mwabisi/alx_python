"""
This module gathers and prints information about the task completion status of all employees.
The employee data is obtained from an API endpoint.
"""

import json
import requests

def get_all_users():
    """
    Fetches data about all the users from an API.

    Returns:
    list(dict): The information about all the users.
    """
    
    user_info = requests.get('https://jsonplaceholder.typicode.com/users').json()
    return user_info

def get_user_tasks(user_id):
    """
    Fetches the tasks of a specific user from an API.

    Args:
    user_id (int): The ID of the user.

    Returns:
    list(dict): The tasks of the user.
    """
    
    todos = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}/todos').json()
    return todos

def write_to_json(users):
    """
    Writes the tasks of all employees to a JSON file.

    Args:
    users (list(dict)): The information about all the employees.
    """

    all_tasks = {}
    for user in users:
        tasks = get_user_tasks(user['id'])
        task_list = [{'username': user['username'], 'task': task['title'], 'completed': task['completed']} for task in tasks]
        all_tasks[user['id']] = task_list

    with open('tasks.json', 'w') as jsonfile:
        json.dump(all_tasks, jsonfile)

if __name__ == "__main__":
    users = get_all_users()
    write_to_json(users)