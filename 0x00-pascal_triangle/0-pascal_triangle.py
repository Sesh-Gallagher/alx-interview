#!/usr/bin/python3
"""
Represents 0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Module that returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    k = []
    if n <= 0:
        return k
    k = [[1]]
    for i in range(1, n):
        temp_list = [1]
        for j in range(len(k[i - 1]) - 1):
            curr = k[i - 1]
            temp_list.append(k[i - 1][j] + k[i - 1][j + 1])
        temp_list.append(1)
        k.append(temp_list)
    return k
