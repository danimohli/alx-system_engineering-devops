#!/usr/bin/python3
"""
An API Request to Reddit for possible Users queries
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to return the num of subscribers for
    a given subreddit. Returns 0 if invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'my_reddit_app'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get('data', {}).get('subscribers', 0)
    return 0
