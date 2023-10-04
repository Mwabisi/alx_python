import csv
import requests
import sys

def get_user_tasks(user_id):
    # Define the URL for the JSONPlaceholder API
    base_url = 'https://jsonplaceholder.typicode.com'
    
    # Send a GET request to retrieve user data
    user_url = f'{base_url}/users/{user_id}'
    user_response = requests.get(user_url)
    
    # Check if the user exists
    if user_response.status_code != 200:
        print(f"User with ID {user_id} not found.")
        return
    
    user_data = user_response.json()
    username = user_data['username']

    # Send a GET request to retrieve user's tasks
    tasks_url = f'{base_url}/todos?userId={user_id}'
    tasks_response = requests.get(tasks_url)
    
    # Check if tasks were retrieved successfully
    if tasks_response.status_code != 200:
        print(f"Failed to retrieve tasks for user with ID {user_id}.")
        return
    
    tasks_data = tasks_response.json()
    
    # Create a CSV file to store the user's tasks
    with open(f'{user_id}.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write the CSV header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        for task in tasks_data:
            task_title = task['title']
            task_completed = task['completed']
            
            # Write the task data to the CSV file
            csv_writer.writerow([str(user_id), username, str(task_completed), task_title])
    
    print(f'Tasks for user with ID {user_id} exported to {user_id}.csv successfully.')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 export_to_CSV.py <USER_ID>')
    else:
        user_id = sys.argv[1]
        get_user_tasks(user_id)
