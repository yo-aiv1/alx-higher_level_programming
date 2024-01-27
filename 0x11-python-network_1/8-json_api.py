#!/usr/bin/python3
"""
send a POST request to an api with the letter as a parameter
and print the response
"""
import requests
import sys


if __name__ == "__main__":
    data = {'q': ""}
    apiurl = "http://0.0.0.0:5000/search_user"
    try:
        if len(sys.argv[1]) != 0:
            data['q'] = sys.argv[1]
    except Exception:
        pass

    request = requests.post(apiurl, data)

    try:
        jsonobject = request.json()
        if not jsonobject:
            print("No result")
        else:
            print("[{}] ".format(jsonobject.get('id')), end='')
            print("{}".format(jsonobject.get('name')))
    except Exception:
        print("Not a valid JSON")
