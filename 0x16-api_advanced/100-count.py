#!/usr/bin/python3
"""
Queries to the Reddit API
list all hot articles recursively
"""


import base64
import json
import re
import requests


def sort_by_key(word_list):
    """
    Sort occurrencies by key
    """
    new_dict = {}
    for word in word_list.keys():
        key = str(word_list[word])
        if key not in new_dict:
            new_dict[key] = [word]
        else:
            new_dict[key].append(word)
    return new_dict


def sort_by_alpha(word_list):
    """
    Sorts words same amounts by alphabetical order
    """
    del word_list["0"]
    sted = sorted(list(word_list.keys()), key=lambda s: int(s))
    keys = list(reversed(sted))
    for key in keys:
        for word in sorted(word_list[key]):
            print("{}: {}".format(word, key))
    return keys


def count_words(subreddit, word_list, after=None):
    """
    List all hot
    generates auth credential and acces_token
    and request subreddit
    """
    user = "saQHHJVroJsJHQ"
    passwd = "AneIovAmD8rm-3rEz_3REVumIb0"
    cred = user + ':' + passwd
    credential = cred.encode('ascii')
    credential = base64.b64encode(credential).decode('ascii')
    ot_cred = requests.auth.HTTPBasicAuth(user, passwd)
    tok_url = "https://www.reddit.com/api/v1/access_token"
    query = {}
    query["grant_type"] = "client_credentials"
    headers = {}
    headers["Authorization"] = "Basic {}".format(credential)
    headers["User-Agent"] = "Que te pasa Calabaza (89/90) es 4321"
    token = requests.post(tok_url,
                          data=query,
                          headers=headers,
                          allow_redirects=False)
    tok = token.json().get("access_token")
    typ = token.json().get("token_type")
    endpoint = "https://oauth.reddit.com/r/{}/hot".format(subreddit)
    query = {}
    if after is not None:
        query["after"] = after
    user_agent = "I like (apples/in/trees)"
    headers = {"User-Agent": user_agent}
    headers["Authorization"] = '{} {}'.format(typ, tok)
    response = requests.get(endpoint,
                            headers=headers,
                            params=query)
    if response.status_code == 200:
        subs = response.json()
        top = subs["data"]["children"]
        if len(top) == 0:
            print()
            return None
        if type(word_list) == list:
            word_list = {oc: 0 for oc in word_list}
        for i, post in enumerate(top):
            for word in word_list.keys():
                pattern = ' ' + word.lower() + ''
                test = ' ' + post["data"]["title"].lower() + ' '
                occurrencies = [n.start() for n in re.finditer(pattern, test)]
                word_list[word] += len(occurrencies)
        if subs["data"]["after"] is None:
            word_list = sort_by_key(word_list)
            word_list = sort_by_alpha(word_list)
            return word_list
        return count_words(subreddit, word_list, subs["data"]["after"])
    else:
        print()
        return None
