#!/usr/bin/python3
""" Returns information about his/her TODO list progress. """
import csv
import requests
import sys


if __name__ == "__main__":
    completed = 0
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    username = requests.get(url + "users/{}".format(user_id)).json()
    username = username.get('username')
    user_id = sys.argv[1]

    with open('{}.csv'.format(user_id), 'w', newline="") as f:
        write = csv.writer(f, quoting=csv.QUOTE_ALL)

        [write.writerow([user_id, username, i.get("completed"),
                        i.get("title")]) for i in todos]
