#!/usr/bin/python3
"""
Export API data for all employees to JSON
"""
import json
import requests

if __name__ == '__main__':
    url_users = 'https://jsonplaceholder.typicode.com/users'
    res = requests.get(url_users)
    users = res.json()

    url_tasks = 'https://jsonplaceholder.typicode.com/todos'
    res = requests.get(url_tasks)
    tasks = res.json()

    all_tasks = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        user_tasks = []

        for task in tasks:
            if task.get('userId') == user_id:
                task_dict = {
                    "username": username,
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                user_tasks.append(task_dict)

        all_tasks[user_id] = user_tasks

    filename = 'todo_all_employees.json'
    with open(filename, 'w') as jsonfile:
        json.dump(all_tasks, jsonfile)
