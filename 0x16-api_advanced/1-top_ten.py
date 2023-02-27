#!/usr/bin/python3
""" Write function that queries the Reddit API and
    prints the titles of the first 10 hot posts
    listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
        prints the titles of the first 10 hot posts
        listed for the given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux"}
    p = {"limit": "10"}
    data = requests.get(url, headers=headers, params=p).json()

    try:
        ch = data.get('data').get('children')

        for i in ch:
            print(i.get('data').get('title'))
    except Exception:
        print(None)
