#!/usr/bin/python3
"""
Queries to the Reddit API
list all hot articles recursively
"""
import base64
import json
import requests


def recurse(subreddit, hot_list=[], after=None):
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
        # print(subs.keys())
        # print(subs["data"].keys())
        # print(subs["kind"])
        # print("====================")
        # print(subs["data"]["after"])
        # print(subs["data"]["before"])
        # print("====================")
        # print(json.dumps(subs, indent=2, sort_keys=True))
        top = subs["data"]["children"]
        if len(top) == 0:
            return None
        for i, post in enumerate(top):
            # print(post["data"]["title"])
            hot_list.append(post["data"]["title"])
        if subs["data"]["after"] is None:
            return hot_list
        return recurse(subreddit, hot_list, subs["data"]["after"])
    else:
        return None
