#!/usr/bin/python3

"""Module to query the Reddit API and return a list containing the titles of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=None, after=""):
    """Recursive function that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit"""
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit, after)
    headers = {"User-Agent": "python3"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    for i in response.json().get("data").get("children"):
        hot_list.append(i.get("data").get("title"))
    after = response.json().get("data").get("after")
    return hot_list if after is None else recurse(subreddit, hot_list, after)
