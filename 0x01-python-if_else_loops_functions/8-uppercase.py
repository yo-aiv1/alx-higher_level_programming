#!/usr/bin/python3
def uppercase(str):
    for char in range(len(str)):
        if (ord(str[char]) in range(65, 89)) or (ord(str[char]) == 32) or (ord(str[char]) in range(48, 58)):
            d = 0
        else:
            d = 32
        print("{:c}".format(ord(str[char]) - d), end='')
    print()
