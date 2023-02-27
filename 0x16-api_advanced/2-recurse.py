#!/usr/bin/python3
""" write function that returns a list containing
    the titles of all hot articles for a given
    subreddit
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
        Returns a list containing the titles
        of all hot articles for a given subreddit
    """
