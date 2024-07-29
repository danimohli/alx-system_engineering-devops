#!/usr/bin/python3
"""
todo_progress.py
This script fetches and displays the TODO list progress for
a given employee ID
and exports the data to a CSV file.
"""

import csv
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


def export_to_csv(employee_id, username, todo_list):
    """
    Export the TODO list to a CSV file.
    """
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            writer.writerow([employee_id, username,
                            task.get('completed'), task.get('title')])


def main(employee_id):
    """
    Main function to fetch and display the TODO list
    progress and export to CSV.
    """
    _name = fetch_employee_name(employee_id)
    todo_list = fetch_todo_list(employee_id)

    total_tasks = len(todo_list)
    done_tasks = [task for task in todo_list if task.get('completed')]
    number = len(done_tasks)

    print(f"Employee {_name} is done with tasks({number}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

    export_to_csv(employee_id, _name, todo_list)


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
