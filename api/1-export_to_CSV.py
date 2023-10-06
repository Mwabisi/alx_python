import csv
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

def export_to_csv(user_info, todos):
    """
    Exports the completed tasks of an employee to a CSV file.

    Args:
    user_info (dict): The information about the employee.
    todos (dict): The tasks of the employee.
    """
    employee_id = user_info.get('id')
    file_name = f'{employee_id}.csv'
    
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for task in todos:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': user_info.get('username'),
                'TASK_COMPLETED_STATUS': task.get('completed'),
                'TASK_TITLE': task.get('title')
            })

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        user_info, todos = get_employee_data(sys.argv[1])
        export_to_csv(user_info, todos)
        print("Data exported to CSV file.")