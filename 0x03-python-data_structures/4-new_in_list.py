#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx <= 0) or ((idx + 1) > len(my_list)):
        return my_list
    else:
        newlist = my_list.copy()
        newlist[idx] = element
    return newlist
