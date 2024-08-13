#!/usr/bin/python3
"""
Recursively queries the Reddit API, parses the titles of all hot articles
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles,
    and counts the occurrences of given keywords. Prints the count in
    descending order and alphabetically for ties.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'my_reddit_app'}
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data', {})
    children = data.get('children', [])

    if not children:
        if not word_count:
            return
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")
        return

    for child in children:
        title = child.get('data', {}).get('title', '').lower()
        for word in word_list:
            word_lower = word.lower()
            word_count[word_lower] = word_count.get(word_lower, 0) +\
                title.split().count(word_lower)

    after = data.get('after')
    if after:
        count_words(subreddit, word_list, after, word_count)
    else:
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")
