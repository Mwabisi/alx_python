import csv
import os
import sys

def file_exists(filename):
    """Check if a file exists."""
    return os.path.exists(filename)

def check_csv_format(filename):
    """
    Check the formatting of the CSV file.
    
    Returns:
        bool: True if the formatting is correct, False otherwise.
    """
    try:
        with open(filename, 'r') as f:
            csv_reader = csv.reader(f)
            header = next(csv_reader)  # Read the header
            return header == ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    except Exception as e:
        return False

def user_info(employee_id):
    csv_filename = f"{employee_id}.csv"

    # Check if the CSV file exists
    if not file_exists(csv_filename):
        print("Number of tasks in CSV: Incorrect")
        return

    # Check the formatting of the CSV file
    if not check_csv_format(csv_filename):
        print("Number of tasks in CSV: Incorrect")
    else:
        print("Number of tasks in CSV: OK")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_info(employee_id)

if __name__ == "__main__":
    main()
