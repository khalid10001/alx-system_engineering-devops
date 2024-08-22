#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys


if __name__ == '__main__':

    user_id = sys.argv[1]
    user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}')
    tasks = requests.get(
        f'https://jsonplaceholder.typicode.com/todos',
        params={"userId": user_id})
    if user.status_code == 200:
        data = user.json()
        tasks = tasks.json()
        user_name = data.get("username")
        with open(f'{user_id}.json', 'w', newline='') as josnfile:
            json.dump({f"{user_id}": [
                {
                    "task": f"{task.get('title')}",
                    "completed": task.get("completed"),
                    "username": user_name
                } for task in tasks]}, josnfile)
