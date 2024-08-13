#!/usr/bin/python3
"""
Recursively quer d Reddit API to return a list of titles of all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API to return a list containing the
    titles of all hot articles for a given subreddit. If no results are
    found or the subreddit is invalid, returns None.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'my_reddit_app'}
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    children = data.get('children', [])

    if not children:
        return hot_list if hot_list else None

    hot_list.extend([child.get('data', {}).get('title') for child in children])

    after = data.get('after')

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
