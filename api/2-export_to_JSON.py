import json
import requests
import sys

def user_info(employee_id):
    # API endpoint URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch user data from the API
    response_user = requests.get(user_url)
    user_data = response_user.json()
    username = user_data["username"]

    # Fetch todo data from the API
    response_todo = requests.get(todo_url)
    todo_data = response_todo.json()

    # Create a list of tasks with the required format
    tasks = [
        {
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        }
        for task in todo_data
    ]

    # Create a dictionary with the user ID as the key and tasks list as the value
    user_info_dict = {
        str(employee_id): tasks
    }

    # Export data to JSON file
    json_filename = f"{employee_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump(user_info_dict, json_file, indent=4)

    # Print the JSON data (optional)
    print(json.dumps(user_info_dict, indent=4))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        user_info(employee_id)
