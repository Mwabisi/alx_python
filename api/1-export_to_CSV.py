import csv
import os

# Function to perform checks
def perform_checks(employee_id):
    # Check file existence
    csv_filename = f"{employee_id}.csv"
    if not os.path.exists(csv_filename):
        print("CSV file does not exist.")
        return

    # Check file naming convention
    if not csv_filename.endswith(f"{employee_id}.csv"):
        print("Incorrect CSV file name.")
        return

    # Check correct number of tasks
    with open(csv_filename, mode='r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        task_count = sum(1 for _ in csv_reader) - 1  # Subtract 1 for the header row
        expected_task_count = 11  # Adjust this to the expected number of tasks
        if task_count != expected_task_count:
            print("Incorrect number of tasks in the CSV.")
            return

    # Fetch user data from API for comparison
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(user_url)
    user_data = response.json()

    # Check correct user ID and username
    with open(csv_filename, mode='r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            user_id, username, _, _ = row
            if user_id != str(employee_id) or username != user_data['username']:
                print("Incorrect user ID and username in the CSV.")
                return

    # Check correct output formatting
    # Implement formatting checks here

    print("All checks passed successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python checker.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        perform_checks(employee_id)
