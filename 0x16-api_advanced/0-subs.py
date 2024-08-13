#!/usr/bin/python3
"""
Subreddit sub-count
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the sub-count of a subreddit
    using Reddit's API
    """
    user_agent = 'assiminee'
    url = "https://www.reddit.com/r/{}.json".format(subreddit)

    headers = {'User-Agent': user_agent}

    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp.status_code != 200:
        return 0

    data = resp.json()['data']
    location = data['children'][0]['data']
    return location['subreddit_subscribers'], 'OK'
