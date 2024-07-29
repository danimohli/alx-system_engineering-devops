#!/usr/bin/python3
"""
Export API data to JSON
"""
import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url_user = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    res = requests.get(url_user)
    user_name = res.json().get('username')

    url_tasks = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    res = requests.get(url_tasks)
    tasks = res.json()

    user_tasks = []
    for task in tasks:
        task_dict = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user_name
        }
        user_tasks.append(task_dict)

    user_tasks_dict = {user_id: user_tasks}

    filename = f'{user_id}.json'
    with open(filename, 'w') as jsonfile:
        json.dump(user_tasks_dict, jsonfile)
