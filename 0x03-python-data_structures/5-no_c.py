#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    for i, letter in enumerate(my_string):
        if (ord(letter) == ord('c')) or (ord(letter) == ord('C')):
            continue
        else:
            new_string.append(letter)
    return ''.join(new_string)
