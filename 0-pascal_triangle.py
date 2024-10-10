#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
        Module returns a list of
         integers representing
          the Pascal's triangle of n
         Returns an empty list if n <= 0
    """

    triangle = []

    if n <= 0:
        return triangle
    for i in range(n):
        temp_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(temp_list)
    return triangle
