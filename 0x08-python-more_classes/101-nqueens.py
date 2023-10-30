#!/usr/bin/python3
"""Summary."""


import sys


def check_if_safe(m_queen, nqueen):
    """Determine if the queens can or can't kill each other.

    Args:
        m_queen: array that has the queens positions
        nqueen: queen number

    Returns:
        True: when queens can't kill each other
        False: when some of the queens can kill

    """
    for i in range(nqueen):

        if m_queen[i] == m_queen[nqueen]:
            return False

        if abs(m_queen[i] - m_queen[nqueen]) == abs(i - nqueen):
            return False

    return True


def print_result(m_queen, nqueen):
    """Print the list with the queens positions.

    Args:
        m_queen: array that has the queens positions
        nqueen: queen number

    """
    res = []

    for i in range(nqueen):
        res.append([i, m_queen[i]])

    print(res)


def Queen(m_queen, nqueen):
    """Recursive function that executes the Backtracking algorithm.

    Args:
        m_queen: array that has the queens positions
        nqueen: queen number

    """
    if nqueen is len(m_queen):
        print_result(m_queen, nqueen)
        return

    m_queen[nqueen] = -1

    while ((m_queen[nqueen] < len(m_queen) - 1)):

        m_queen[nqueen] += 1

        if check_if_safe(m_queen, nqueen) is True:

            if nqueen is not len(m_queen):
                Queen(m_queen, nqueen + 1)


def nqueensolution(size):
    """Invoke the Backtracking algorithm.

    Args:
        size: size of the chessboard

    """
    m_queen = [-1 for i in range(size)]

    Queen(m_queen, 0)


if len(sys.argv) == 1 or len(sys.argv) > 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    size = int(sys.argv[1])
except Exception:
    print("N must be a number")
    sys.exit(1)

if size < 4:
    print("N must be at least 4")
    sys.exit(1)

nqueensolution(size)
