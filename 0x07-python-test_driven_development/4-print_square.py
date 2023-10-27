#!/usr/bin/python3
"""summary."""


def print_square(size):
    """Print square.

    Args:
        size (int): size of the square.
    """
    if isinstance(size, int):
        if size < 0:
            raise ValueError("size must be >= 0")
        for i in range(size):
            for j in range(size):
                print("#", end='')
            print()
    else:
        raise TypeError("size must be an integer")
