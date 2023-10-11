#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, val in dict(a_dictionary).items():
        if val == value:
            del a_dictionary[key]
        elif val != value:
            continue
    return (a_dictionary)