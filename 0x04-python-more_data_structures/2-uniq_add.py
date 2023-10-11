#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    nums = []

    for num in my_list:
        if num in nums:
            continue
        else:
            nums.append(num)

    for num in nums:
        result += num

    return result
