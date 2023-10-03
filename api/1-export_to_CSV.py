import csv
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

        # Create and write data to CSV file
        csv_filename = f"{user_data['id']}.csv"
        with open(csv_filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # Write the header row
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            # Write task records
            for task in todos_data:
                csv_writer.writerow([user_data['id'], user_data['username'], task['completed'], task['title']])

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
