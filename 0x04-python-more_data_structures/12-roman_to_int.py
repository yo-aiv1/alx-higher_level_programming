#!/usr/bin/python3
def roman_to_int(roman_string):
    dir = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    nums = []
    result = 0
    if roman_string == None:
        return 0

    for i, char in enumerate(roman_string):
        if char in dir.keys():
            nums.append(dir[char])

    for i in range(len(nums)):
        if i == len(nums) - 1:
            result += int(nums[i])
        elif nums[i] == nums[i + 1]:
            result += int(nums[i])
        elif nums[i] > nums[i + 1]:
            result += int(nums[i])
        elif nums[i] < nums[i + 1]:
            result -= int(nums[i])

    return (result)
