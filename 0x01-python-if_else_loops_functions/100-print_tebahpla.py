#!/usr/bin/python3
def check(num):
    if num in range(121, 98, -1):
        return 32
    else:
        return 0
for i in range(122, 96, -1):
    if i % 2 == 0:
        print(chr(i), end='')
    else:
        print("{}".format(chr(i - 32)), end='')
