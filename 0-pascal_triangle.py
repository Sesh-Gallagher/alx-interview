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

    if n <= 0:
        return []
    triangle = [[1]]
    for a in range(1, n):
<<<<<<< HEAD
        row = [1]
=======
        row = [1] 
>>>>>>> 1dd1a3dce0f8d6ce2be415142311da268616d33e
        for b in range(1, a):
            row.append(triangle[a - 1][b - 1] + triangle[a - 1][b])
        row.append(1)
        triangle.append(row)
<<<<<<< HEAD
    return triangle
=======
    return triangle 
>>>>>>> 1dd1a3dce0f8d6ce2be415142311da268616d33e
