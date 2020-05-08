#!/usr/bin/python3
"""
Queries to the Reddit API
list hot top ten
"""
import base64
import json
import requests


def top_ten(subreddit):
    """
    List the top ten
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
    user_agent = "I like (apples/in/trees)"
    headers = {"User-Agent": user_agent}
    headers["Authorization"] = '{} {}'.format(typ, tok)
    query["sr_fullname"] = subreddit
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        subs = response.json()
        # print(json.dumps(subs, indent=2, sort_keys=True))
        top = subs["data"]["children"][:10]
        if len(top) == 0:
            print("None")
            return
        for i, post in enumerate(top):
            print(post["data"]["title"])
    else:
        print("None")
