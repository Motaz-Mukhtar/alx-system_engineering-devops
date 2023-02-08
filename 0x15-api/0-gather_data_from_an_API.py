#!/usr/bin/python3
""" Returns information about his/her TODO list progress. """
import requests
import sys


if __name__ == "__main__":
    completed = 0
    my_list = []
    todos = requests.get(f"https://jsonplaceholder.typicode.com/\
                         todos?userId={sys.argv[1]}")
    user = requests.get(f"https://jsonplace\
                        holder.typicode.com/users/{sys.argv[1]}")
    for obj in todos.json():
        my_list.append(obj['title'])
        if obj['completed'] is True:
            completed = completed + 1
    username = user.json()['name']
    print("Employee {} is done with tasks({\
          }/{}):".format(username, completed, len(todos.json())))
    for title in my_list:
        print('\t', title)
