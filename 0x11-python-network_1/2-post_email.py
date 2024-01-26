#!/usr/bin/python3
""" send a post script to a website with parameter and print response """
from urllib import request, parse
import sys


if __name__ == "__main__":
    parameter = {'email': sys.argv[2]}
    data = parse.urlencode(parameter)
    data = data.encode('ascii')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
