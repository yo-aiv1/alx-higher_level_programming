#!/usr/bin/python3
def best_score(a_dictionary):
    values = []
    if a_dictionary is None:
        return None
    for k, v in a_dictionary.items():
        values.append(v)
    for key, value in a_dictionary.items():
        if value == max(values):
            return key
