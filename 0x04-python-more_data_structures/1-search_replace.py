#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_listc = my_list.copy()
    for i, char in enumerate(my_listc):
        if char == search:
            my_listc[i] = replace

    return my_listc
