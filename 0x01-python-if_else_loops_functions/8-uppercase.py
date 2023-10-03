#!/usr/bin/python3
def uppercase(str):
    for char in range(len(str)):
        if ord(str[char]) not in range(97, 122):
            d = 0
        else:
            d = 32
        print("{:c}".format(ord(str[char]) - d), end='')
    print()
