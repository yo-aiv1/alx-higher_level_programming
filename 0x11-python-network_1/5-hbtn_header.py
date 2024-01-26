#!/usr/bin/python3
""" Fetch and print the X-Request-Id from the header """
import requests
import sys


if __name__ == "__main__":
    request = requests.get(sys.argv[1])
    print(request.headers['X-Request-Id'])
