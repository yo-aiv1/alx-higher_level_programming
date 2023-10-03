#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
strat = 0
if number < 0:
    number *= -1
    strat = 1
last_digit = number % 10
if strat == 1:
    number *= -1
    last_digit *= -1
print(f"Last digit of {number} is ", end="")
if last_digit > 5:
    print(f"{last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"{last_digit} and is 0")
else:
    print(f"{last_digit} and is less than 6 and not 0")
