#!/usr/bin/python3
""" Modules to query the Reddit API and return the titles of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Function to return the number of subscribers"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "python3"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        for i in response.json().get("data").get("children"):
            print(i.get("data").get("title"))
    else:
        print("None")
