import requests
import sys


def fetch_employee_data(employee_id):
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

        # Calculate the number of completed tasks
        completed_tasks = [task for task in todos_data if task["completed"]]
        num_completed_tasks = len(completed_tasks)
        total_num_tasks = len(todos_data)

        # Display employee TODO list progress with the correct formatting
        print(f"{user_data['name']} is done with {num_completed_tasks}/{total_num_tasks} tasks:")
        for task in todos_data:
            print_task_status(task)

    except requests.exceptions.RequestException as e:
        print("Error: Unable to fetch data from the API.")
        print(e)


def print_task_status(task):
    task_status = "✓" if task["completed"] else "✗"
    print(f"{task_status} {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        fetch_employee_data(employee_id)
