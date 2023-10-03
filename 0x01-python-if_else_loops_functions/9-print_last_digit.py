#!/usr/bin/python3
def print_last_digit(number):
        if number >= 0:
            last = number % 10
            print(last, end='')
        else:
            last = int(str(number)[-1])
            print(int(str(number)[-1]), end='')
        return last
