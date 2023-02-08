#!/usr/bin/python3
""" Returns Records all tasks from all employees """
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open('todo_all_employees.json', 'w') as f:
        json.dump({user.get('id'): [{
            "username": i.get('username'),
            "task": i.get('title'),
            "completed": i.get('completed')
            } for i in requests.get(url + 'todos', params={"user_id": user.get('id')}
                ).json()] for user in users }, f)
