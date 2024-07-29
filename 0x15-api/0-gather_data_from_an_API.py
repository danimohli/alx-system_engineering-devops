#!/usr/bin/python3
"""
todo_progress.py
This script fetches and displays the TODO list
progress for a given employee ID.
"""

import requests
import sys


def fetch_employee_name(employee_id):
    """
    Fetch the employee's name using the employee ID.
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    user = response.json()
    return user.get('name')


def fetch_todo_list(employee_id):
    """
    Fetch the TODO list for the given employee ID.
    """
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)
    return response.json()


def main(employee_id):
    """
    Main function to fetch and display the TODO list progress.
    """
    employee_name = fetch_employee_name(employee_id)
    todo_list = fetch_todo_list(employee_id)

    total_tasks = len(todo_list)
    done_tasks = [task for task in todo_list if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    tast = '{number_of_done_tasks}/{total_tasks}'
    print(f"Employee {employee_name} is done with tasks(tast):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./todo_progress.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    main(employee_id)
