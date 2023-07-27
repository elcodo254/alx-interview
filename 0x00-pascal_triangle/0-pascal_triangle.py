#!/usr/bin/python3
"""
Module for Pascal's triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing pascal's triangle
    """

    if n <= 0:
        return []

    triangle = [[] for index in range(n)]
    for line in range(n):
        for col in range(line+1):
            if(col < line):
                if(col == 0):
                    """ the first column is always set to 1 """
                    triangle[line].append(1)
                else:
                    triangle[line].append(triangle[line-1][col]
                                          + triangle[line-1][col-1])
            elif(col == line):
                """ the diagonal is always set to 1 """
                triangle[line].append(1)

    return triangle
