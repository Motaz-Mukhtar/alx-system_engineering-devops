#!/usr/bin/python3
""" write function that returns a list containing
    the titles of all hot articles for a given
    subreddit
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=""):
    """
        Returns a list containing the titles
        of all hot articles for a given subreddit
    """
    params = {
        "after": after,
        "count": count,
        "limits": 100
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux"}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        return None

    data = response.json().get('data')
    after = data.get('after')
    count += data.get('dist')

    for i in data.get('children'):
        hot_list.append(i.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, count, after)

    return hot_list
