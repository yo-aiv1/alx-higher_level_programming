#!/usr/bin/python3
"""summary."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix (_type_): list of lists
        div (_type_): num

    Returns:
        _type_: list of lists
    """
    message1 = "matrix must be a matrix (list of lists) of integers/floats"
    message2 = "exception with the message division by zero"

    if not isinstance(matrix, list):
        raise TypeError(message1)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div <= 0:
        raise ZeroDivisionError(message2)
    
    for i in matrix:
        if type(i) is not list:
            raise TypeError(message1)

    result = []
    size = len(matrix[0])

    for lst in matrix:

        if len(lst) != size:
            raise TypeError("Each row of the matrix must have the same size")

        new = []
        for i in lst:

            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError(message1)

            m = i / div

            new.append(round(m, 2))
        result.append(new)

    return result
