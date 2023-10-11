#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    elments = []
    for i in set_2:
        if i in set_1:
            continue
        else:
            elments.append(i)

        for i in set_1:
            if (i in set_2) or (i in elments):
                continue
            else:
                elments.append(i)

    return (elments)
