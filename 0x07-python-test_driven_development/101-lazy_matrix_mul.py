#!/usr/bin/python3.5
"""summary."""


import numpy as np
def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices using numpy.

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multiplication


    """
    if type(m_a) is not list or type(m_b) is not list:
        raise TypeError('must give a list of integets')
    for i in m_a:
        if type(i) is not list:
            raise TypeError('must give a list of integets')
    for j in m_b:
        if type(j) is not list:
            raise TypeError('must give a list of integets')

    return (np.matmul(m_a, m_b))
