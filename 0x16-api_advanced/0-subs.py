#!/usr/bin/python3
"""
Queries to the Reddit API
request for subscribers
"""
import base64
import json
import requests


def number_of_subscribers(subreddit):
    """
    List and count the amount of subscribers for the given subreddit
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
    endpoint = "https://oauth.reddit.com/api/search_subreddits"
    query = {}
    user_agent = "I like (apples/in/trees)"
    headers = {"User-Agent": user_agent}
    headers["Authorization"] = '{} {}'.format(typ, tok)
    query["query"] = subreddit
    query["exact"] = True
    query["include_over_18"] = True
    response = requests.post(endpoint, data=query, headers=headers)
    if response.status_code == 200:
        subs = response.json()
        # print(json.dumps(subs, indent=2))
        count = 0
        for sub in subs["subreddits"]:
            count += sub["subscriber_count"]
        return count
    else:
        return 0
