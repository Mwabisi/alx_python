import requests

def get_employee_todo_list_progress(employee_id):
    """Returns information about the employee's TODO list progress.

    Args:
        employee_id: The ID of the employee.

    Returns:
        A string containing the employee's TODO list progress.
    """

    # Get the employee's TODO list items.
    response_todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    
    if response_todos.status_code != 200:
        raise Exception(f"Failed to retrieve TODO list items for employee {employee_id}.")
    
    todo_list_items = response_todos.json()

    # Get the employee's name.
    response_employee = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    
    if response_employee.status_code != 200:
        raise Exception(f"Failed to retrieve employee information for ID {employee_id}.")
    
    employee = response_employee.json()
    employee_name = employee["name"]

    # Calculate the number of completed tasks.
    number_of_done_tasks = sum(1 for item in todo_list_items if item["completed"])

    # Calculate the total number of tasks.
    total_number_of_tasks = len(todo_list_items)

    # Generate the output string.
    output_string = f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):\n"
    
    # Include completed tasks in the output.
    for todo_list_item in todo_list_items:
        if todo_list_item["completed"]:
            output_string += f"  {todo_list_item['title']}\n"

    return output_string

if __name__ == "__main__":
    try:
        # Get the employee ID from the user.
        employee_id = int(input("Enter the employee ID: "))

        # Get the employee's TODO list progress.
        employee_todo_list_progress = get_employee_todo_list_progress(employee_id)

        # Print the employee's TODO list progress to the console.
        print(employee_todo_list_progress)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
