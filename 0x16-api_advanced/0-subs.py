#!/usr/bin/python3
""" write function that queries the Reddit API
    and returns the number of subscribers
"""
import sys
import requests


def number_of_subscribers(subreddit):
    """ Return the number of Subscribers in subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux"}

    data = requests.get(url, headers=headers).json()
    try:
        num_of_sub = data.get('data').get('subscribers')
    except Exception:
        return 0

    if num_of_sub is None or not num_of_sub:
        return 0

    return num_of_sub
