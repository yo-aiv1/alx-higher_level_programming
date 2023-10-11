#!/usr/bin/python3
def common_elements(set_1, set_2):
    elments = []
    for i in set_1:
        if i not in set_2:
            continue
        else:
            elments.append(i)
    return (elments)
