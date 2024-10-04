#!/usr/bin/python3

"""
0-pascal_triangle
"""


def pascal_triangle(n):

"""
Modulle that returns a list of integers that
    represent the Pascal Triangle of n
    returns empty list if n <= 0
"""

    a = []
    if n <= 0:
        return a
    a = [[1]]
    for b in range(1, n):
        temp = [1]
        for c in range(len(a[b - 1]) - 1):
            curr = a[b - 1]
            temp.append(a[b - 1][c] + a[b - 1][c + 1])
        temp.append(1)
        a.append(temp)
    return a
