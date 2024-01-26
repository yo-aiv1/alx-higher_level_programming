#!/usr/bin/python3
""" send a post script to a website with parameter and print response """
import requests
import sys


if __name__ == "__main__":
    parameter = {'email': sys.argv[2]}
    request = requests.post(sys.argv[1], data=parameter)
    print(request.text)
