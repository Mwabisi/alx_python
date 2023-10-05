import requests

def get_todo_progress(employee_id):
    """
    Get and print the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.
    """

    # Send a GET request to the REST API to fetch the TODO list for the given employee ID.
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")

    # Convert the response to JSON format. This gives us a list of TODO items.
    todos = response.json()

    # Count the number of completed TODO items by summing up the 'completed' field of each TODO item.
    completed_count = sum(todo['completed'] for todo in todos)

    # Get the total number of TODO items.
    total_count = len(todos)

    # Print the employee ID.
    print(f"Employee ID: {employee_id}")

    # Print the total number of TODO items.
    print(f"Total TODOs: {total_count}")

    # Print the number of completed TODO items.
    print(f"TODOs completed: {completed_count}")

    # Calculate and print the progress as the percentage of completed TODO items out of the total.
    print(f"Progress: {completed_count / total_count * 100:.2f}%")

# Call the function with an example employee ID.
get_todo_progress(1)
This function accepts an employee ID as an argument, fetches the TODO list for that employee from the REST API, counts the