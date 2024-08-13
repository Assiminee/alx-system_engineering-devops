#!/usr/bin/python3
"""Queries Reddit API
"""
import requests


def top_ten(subreddit):
    """
    Queries Reddit API to find top 10 posts
    on a subreddit
    """

    user_agent = '0x16-api_advanced-assiminee'
    endpoint = '/r/{}/hot.json?limit=10'.format(subreddit)

    headers = {'User-Agent': user_agent}

    r = requests.get(
        'https://www.reddit.com{}'.format(endpoint),
        headers=headers, allow_redirects=False
        )

    if r.status_code != 200:
        print('None')
        return

    data = r.json()['data']
    posts = data['children']
    for post in posts:
        print(post['data']['title'])
