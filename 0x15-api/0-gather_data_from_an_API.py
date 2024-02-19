#!/usr/bin/python3

import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    todos_url = f'{base_url}/todos?userId={employee_id}'
    user_url = f'{base_url}/users/{employee_id}'
    
    # Fetching user info
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data['name']
    
    # Fetching todos
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    # Counting completed tasks
    total_tasks = len(todos_data)
    completed_tasks = [todo for todo in todos_data if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    
    # Displaying progress
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
        
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)