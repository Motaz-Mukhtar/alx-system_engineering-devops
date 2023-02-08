#!/usr/bin/python3
""" Export data in the CSV format. """
import requests
import sys
import json


if __name__ == "__main__":
    completed = 0
    url = "https://jsonplaceholder.typicode.com"
    todos = requests.get(url + "/todos?userId={}".format(sys.argv[1]))
    user = requests.get(url + "/users/{}".format(sys.argv[1]))
    username = user.json().get('username')

    with open(f'{sys.argv[1]}.json', mode='w') as f:
        for obj in todos.json():
            completed = obj.get('completed')
            title = obj.get('title')
            str1 = "\"{}\",\"{}\",".format(sys.argv[1], username)
            str2 = "\"{}\",\"{}\"\n".format(completed, title)
            string = str1 + str2
            f.write(string)
