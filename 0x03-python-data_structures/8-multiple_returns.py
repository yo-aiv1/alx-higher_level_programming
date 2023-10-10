#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) <= 0:
        firstc = (None)
    else:
        firstc = (sentence[0])
    return ((len(sentence)), firstc)
