#!/usr/bin/python3
""" Returns information about his/her TODO list progress. """
import requests
import sys


if __name__ == "__main__":
    completed = 0
    url = "https://jsonplaceholder.typicode.com"
    my_list = []
    todos = requests.get(url + "/todos?userId={}".format(sys.argv[1]))
    user = requests.get(url + "/users/{}".format(sys.argv[1]))
    for obj in todos.json():
        my_list.append(obj.get('title'))
        if obj.get('completed') is True:
            completed = completed + 1
    username = user.json().get('name')
    emp = "Emplyee {} is done with tasks ".format(username)
    print(emp + "({}/{}):".format(completed, len(todos.json())))
    for title in my_list:
        print('\t', title)
