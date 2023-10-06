#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import sub, mul, div, add
    if (len(sys.argv) - 1) != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)

    first = int(sys.argv[1])
    second = int(sys.argv[3])

    if '+' in sys.argv[2]:
        print("{} + {} = {}".format(first, second, add(int(sys.argv[1]), int(sys.argv[3]))))
    elif '-' in sys.argv[2]:
        print("{} - {} = {}".format(first, second, sub(int(sys.argv[1]), int(sys.argv[3]))))
    elif '*' in sys.argv[2]:
        print("{} * {} = {}".format(first, second, mul(int(sys.argv[1]), int(sys.argv[3]))))
    elif '/' in sys.argv[2]:
        print("{} / {} = {}".format(first, second, div(int(sys.argv[1]), int(sys.argv[3]))))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
