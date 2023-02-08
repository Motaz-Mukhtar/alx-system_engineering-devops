#!/usr/bin/python3
""" Records all tasks that are owned by this employee """
import json
import requests
import sys


if __name__ == "__main__":
    my_list = []
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    username = requests.get(url + "users/{}".format(user_id)).json()
    username = username.get('username')
    user_id = sys.argv[1]

    with open('{}.json'.format(user_id), 'w') as f:
        for obj in todos:
            my_dict = {}
            my_dict['task'] = obj.get('title')
            my_dict['completed'] = obj.get('completed')
            my_dict['username'] = username
            my_list.append(my_dict)
        f.write(json.dumps({user_id: my_list}))
