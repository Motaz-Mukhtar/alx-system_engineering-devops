#!/usr/bin/python3
""" Returns information about his/her TODO list progress. """
import requests
import sys


if __name__ == "__main__":
    completed = 0
    url = "https://jsonplaceholder.typicode.com/"
    my_list = []
    user_id = sys.argv[1]
    todos = requests.get(url + "todos", params={"userId": user_id})
    user = requests.get(url + "users/{}".format(user_id))

    for obj in todos.json():
        if obj.get('completed') is True:
            my_list.append(obj.get('title'))
    username = user.json().get('name')
    emp = "Employee {} is done with tasks ".format(username)
    print(emp + "({}/{}):".format(len(my_list), len(todos.json())))
    for title in my_list:
        print('\t', title)
