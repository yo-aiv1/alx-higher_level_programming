#!/usr/bin/python3
""" Fetch and print response and print http error code if something worng """
import requests
import sys


if __name__ == "__main__":
    request = requests.get(sys.argv[1])
    code = request.status_code
    if code == 200:
        print(request.text)
    else:
        print("Error code: {}".format(code))
