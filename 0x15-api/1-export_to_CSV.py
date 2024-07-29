#!/usr/bin/python3
"""
todo_progress.py
This script fetches and displays the TODO list progress for a given employee ID
and exports the data to a CSV file.
"""

import csv
import requests
import sys


def fetch_employee_data(employee_id):
    """
    Fetch the employee's data using the employee ID.
    """
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    dos_ = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    user_data = user_response.json()
    todos_response = requests.get(dos_)
    todos_data = todos_response.json()

    return user_data[0], todos_data


def export_to_csv(employee_id, username, todos):
    """
    Export the TODO list to a CSV file.
    """
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, username,
                            task.get('completed'), task.get('title')])


def main(employee_id):
    """
    Main function to fetch and display the TODO list progress
    and export to CSV.
    """
    user_data, todos = fetch_employee_data(employee_id)
    _name = user_data.get('username')

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get('completed')]
    _done_ = len(done_tasks)

    print(f"Employee {_name} is done with tasks({_done_}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

    export_to_csv(employee_id, _name, todos)


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
