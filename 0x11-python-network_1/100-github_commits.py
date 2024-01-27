#!/usr/bin/python3
"""
fetch the last 10 commits of a repository in github
using Github API
"""
from requests import get, auth
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    apiurl = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    request = get(apiurl)
    jsonobject = request.json()
    try:
        for i in range(0, 10):
            sha = jsonobject[i].get('sha')
            name = jsonobject[i].get('commit').get('author').get('name')
            print("{}: {}".format(sha, name))
    except Exception:
        pass
