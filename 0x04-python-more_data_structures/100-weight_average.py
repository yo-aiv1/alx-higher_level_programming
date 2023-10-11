#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    sub = 0
    if len(my_list) == 0:
        return (0)
    for i in my_list:
        num += (i[0] * i[1])
        sub += i[1]
    return (num / sub)
