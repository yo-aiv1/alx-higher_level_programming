#!/usr/bin/python3
""" function that find peak in a list of integers """


def find_peak(list_of_integers):
    lenght = len(list_of_integers)
    IntList = list_of_integers
    if IntList is None or lenght < 3:
        return None
    for i in range(lenght - 1):
        if IntList[i - 1] < IntList[i] > IntList[i + 1]:
            return IntList[i]
