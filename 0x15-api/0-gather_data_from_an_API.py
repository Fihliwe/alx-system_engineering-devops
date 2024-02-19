#!/usr/bin/python3

import requests
import sys

def todo_progress(employee_id):
    """
    Method to display on the standard output the employee TODO list progress
    """
    
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        todos = response.json()
        
        completed_tasks = [todo['title'] for todo in todos if todo['completed']]
        
        total_tasks = len(todos)
        
        num_completed = len(completed_tasks)
        
        employee_name = todos[0]['name']
        
        print(f"Employee {employee_name} is done with tasks ({num_completed}/{total_tasks}):")
        
        for task  in completed_tasks:
            print(f"\t{task}")
        else:
            print("Failed to retrieve data. Please try again later.")
            

if __name__ =="__main__":
    if len(sys.argv) !=2:
        print("Usage python script.py <employee_id>")
        sys.exit(1)
        
    employee_id = sys.argv[1]
    todo_progress(employee_id)