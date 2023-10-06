#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print(a, "{}".format('+'), b, "{}".format('='), add(a, b))
    print(a, "{}".format('-'), b, "{}".format('='), sub(a, b))
    print(a, "{}".format('*'), b, "{}".format('='), mul(a, b))
    print(a, "{}".format('/'), b, "{}".format('='), div(a, b))
