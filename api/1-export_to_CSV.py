import csv
import requests
import sys
import os  # Import the os module to check if the file exists

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
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for task in todos_data:
                csv_writer.writerow([user_data['id'], user_data['name'], task['completed'], task['title']])

        print(f"Data has been exported to {csv_filename}.")

        # Now, perform the checks after creating the CSV file
        if os.path.isfile(csv_filename):
            # Check number of tasks in CSV
            with open(csv_filename, 'r') as f:
                num_tasks = sum(1 for _ in f) - 1  # Subtract 1 for the header row
                print(f"Number of tasks in CSV: {num_tasks} (excluding header)")

            # Check user ID and username
            if user_data['id'] == int(csv_filename.split('.')[0]) and user_data['name'] in open(csv_filename).read():
                print("User ID and Username: OK")

            # Check formatting
            with open(csv_filename, 'r') as f:
                for line in f.readlines():
                    if not line.strip().endswith('"'):
                        print("Formatting: Incorrect")
                        break
                else:
                    print("Formatting: OK")

    except requests.exceptions.RequestException as e:
        print("Error: Unable to fetch data from the API.")
        print(e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        fetch_employee_data(employee_id)
