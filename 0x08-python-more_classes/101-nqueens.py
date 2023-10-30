#!/usr/bin/python3
"""Summary."""

import sys
global N
N = 4


def printSolution(board):
    """Print the list with the queens positions.

    Args:
        board: array that has the queens positions

    """
    for i in range(N):
        for j in range(N):
            print(board[i][j])
        print


def check_if_safe(board, row, col):
    """Determine if the queens can or can't kill each other.

    Args:
        board: array that has the queens positions
        row: queen number
        col: int

    Returns:
        True: when queens can't kill each other
        False: when some of the queens can kill

    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solvequeens(board, col):
    """Recursive function that executes the Backtracking algorithm.

    Args:
        board: array that has the queens positions
        col: queen number

    """
    if type(N) is not int:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)

    if col >= N:
        return True

    for i in range(N):

        if check_if_safe(board, i, col):
            board[i][col] = 1

            if (solvequeens(board, col + 1)):
                return True

            board[i][col] = 0

    return False


def solve():
    """Invoke the Backtracking algorithm."""
    board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    if not solvequeens(board, 0):
        print("Solution does not exist")
        return False

    printSolution(board)
    return True
