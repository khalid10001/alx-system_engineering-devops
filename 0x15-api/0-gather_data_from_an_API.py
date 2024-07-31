#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


if __name__ == '__main__':

    user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}')
    tasks = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos')
    done_tasks = []
    if user.status_code == 200:
        data = user.json()
        tasks = tasks.json()
        all_tasks = len(tasks)
        for task in tasks:
            if task.get("completed") is True:
                done_tasks.append(task.get("title"))
        print(f'Employee {data.get("name")} is done '
              f'with tasks({len(done_tasks)}/{all_tasks}):')
        print('\n'.join('\t ' + task for task in done_tasks))
