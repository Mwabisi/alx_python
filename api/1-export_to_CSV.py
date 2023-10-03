import requests
import csv
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

        # Display employee TODO list progress with the correct formatting
        print(f"{user_data['name']} is done with {len(completed_tasks)}/{len(todos_data)} tasks:")
        for task in completed_tasks:
            print(f"\t{task['title']}")

        # Export data to CSV file
        csv_filename = f"{user_data['id']}.csv"
        with open(csv_filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for task in todos_data:
                csv_writer.writerow([user_data['id'], user_data['name'], str(task['completed']), task['title']])
        
        print(f"Data has been exported to {csv_filename}.")

    except requests.exceptions.RequestException as e:
        print("Error: Unable to fetch data from the API.")
        print(e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        fetch_employee_data(employee_id)
