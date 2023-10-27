#!/usr/bin/python3
"""summary."""


def add_integer(a, b=98):
    """Add 2 integers.

    Args:
        a (int): integer to add.
        b (int): integer to add. Defaults to 98.
    Returns:
        int: result of adding a and b.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
