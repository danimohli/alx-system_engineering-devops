#!/usr/bin/python3
import requests
"""
An API Request to Reddit for possible Users querie
"""


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to return the num of subscribers for
    a given subreddit.
    """
    url = 'https://reddit.com/r/' + subreddit + '/about/.json'
    headers = {'User-Agent': "lala"}
    r = requests.get(url, headers=headers)
    try:
        return(r.json().get('data').get('subscribers'))
    except Exception:
        return(0)
