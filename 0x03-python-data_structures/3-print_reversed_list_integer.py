#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return None
    elif len(my_list) == 0:
        return None
    else:
        for i in range(len(my_list)):
            if i == 0:
                continue
            print("{:d}".format(my_list[-i]))
        print("{:d}".format(my_list[0]))
