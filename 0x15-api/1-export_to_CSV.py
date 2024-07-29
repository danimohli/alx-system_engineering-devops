#!/usr/bin/python3
"""
todo_progress.py
This script fetches and displays the TODO list
progress for a given employee ID
and exports the data to a CSV file.
"""
import csv
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user_id
    res = requests.get(url_user)
    user_name = res.json().get('username')

    url_ = 'https://jsonplaceholder.typicode.com/users/' + user_id + '/todos'
    res = requests.get(url_)
    tasks = res.json()

    with open('{}.csv'.format(user_id), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            user_id = task.get('userId')
            completed = task.get('completed')
            title_task = task.get('title')
            writer.writerow([user_id, user_name, completed, title_task])
