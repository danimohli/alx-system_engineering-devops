#!/usr/bin/python3
"""
An API Request to Reddit for possible
Users queries
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to return the number of subscribers for
    a given subreddit.
    If the subreddit is invalid, returns 0.

    Parameters:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers or 0 if the subreddit is invalid.
    """
    headers = {
        'User-Agent': 'my_reddit_app'
    }

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    elif response.status_code == 302:
        return 0
    else:
        return 0
