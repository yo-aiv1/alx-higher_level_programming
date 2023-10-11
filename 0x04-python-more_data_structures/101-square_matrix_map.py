#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    matrix1 = matrix.copy()
    for i in range(len(matrix)):
        matrix1[i] = list(map(lambda x: x**2, matrix[i]))

    return matrix1
