#!/usr/bin/python3
""" Fetch and print response and print http error code if something worng """
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error ode: {}".format(err.code))
