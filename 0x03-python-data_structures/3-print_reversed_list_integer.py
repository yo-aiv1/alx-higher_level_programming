#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        if i == 0:
            continue
        print("{}".format(my_list[-i]))
    print("{}".format(my_list[0]))
