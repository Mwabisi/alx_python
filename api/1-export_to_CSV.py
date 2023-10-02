import csv
import requests
import sys

def fetch_employee_data(employee_id):
    # URL for employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    # URL for employee's TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    try:
        # Fetch employee details
        employee_response = requests.get(employee_url)
        employee_response.raise_for_status()
        employee_data = employee_response.json()

        # Fetch TODO list
        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()
        todo_data = todo_response.json()

        return employee_data, todo_data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

def export_to_csv(employee_id, employee_data, todo_data):
    filename = f"{employee_id}.csv"

    with open(filename, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_data:
            completed_status = "True" if task["completed"] else "False"
            csv_writer.writerow([employee_id, employee_data["username"], completed_status, task["title"]])

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_data, todo_data = fetch_employee_data(employee_id)

    export_to_csv(employee_id, employee_data, todo_data)

if __name__ == "__main__":
    main()
