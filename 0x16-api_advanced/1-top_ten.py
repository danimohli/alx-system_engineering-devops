#!/usr/bin/python3
"""
Top ten reddit hot post.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. If the subreddit is invalid, prints None.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'my_reddit_app'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json().get('data', {}).get('children', [])
        for post in posts:
            print(post.get('data', {}).get('title'))
    else:
        print(None)
