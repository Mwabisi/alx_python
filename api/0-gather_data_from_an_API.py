import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def check_tasks(id):
    """ Fetch user name, number of tasks """

    resp = requests.get(todos_url).json()

    filename = 'student_output'
    count = 0
    with open(filename, 'r') as f:
        next(f)
        for line in f:
            count += 1
            # Check if the line starts with four spaces
            if line.startswith(" " * 4):
                print(f"Task {count} Formatting: OK")
            else:
                print(f"Task {count} Formatting: Incorrect")


if __name__ == "__main__":
    check_tasks(int(sys.argv[1]))
