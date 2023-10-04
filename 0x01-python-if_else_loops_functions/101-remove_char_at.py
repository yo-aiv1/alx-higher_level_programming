#!/usr/bin/python3
def remove_char_at(str, n):
    num = ""
    for i, letter in enumerate(str):
        if i != n:
            num += letter
    return num
