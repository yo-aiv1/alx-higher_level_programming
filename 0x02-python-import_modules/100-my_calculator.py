#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import sub, mul, div, add
    if len(sys.argv) > 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    else:
        if '+' in sys.argv[2]:
            print("{} + {} = {}".format(int(sys.argv[1]), int(sys.argv[3]), add(int(sys.argv[1]), int(sys.argv[3]))))
        elif '-' in sys.argv[2]:
            print("{} - {} = {}".format(int(sys.argv[1]), int(sys.argv[3]), sub(int(sys.argv[1]), int(sys.argv[3]))))
        elif '*' in sys.argv[2]:
            print("{} * {} = {}".format(int(sys.argv[1]), int(sys.argv[3]), mul(int(sys.argv[1]), int(sys.argv[3]))))
        elif '/' in sys.argv[2]:
            print("{} / {} = {}".format(int(sys.argv[1]), int(sys.argv[3]), div(int(sys.argv[1]), int(sys.argv[3]))))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
