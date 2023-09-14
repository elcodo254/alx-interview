#!/usr/bin/env python3
"""
module that rotates a 2d matrix at 90 degrees
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a  2D matrix in its place
    """
    n = len(matrix)
    order = []

    for i in range(n):
        for j in range(n-1, -1, -1):
            order.append(matrix[j][i])

    for i in range(n):
        for j in range(n):
            matrix[i][j] = order.pop(0)
