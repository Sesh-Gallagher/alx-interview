#!/usr/bin/python3
"""
Island Perimeter Problem module
"""


def island_perimeter(grid):
    """
    Calculate and return perimeter of island in the grid
    Grid is a rectangular grid where 0s represent water and 1s represent land
    Each cell is a square with a side length of 1
    There is only one island
    Args: grid [list] : 2d list of ints either 0 or 1
    Return: perimeter of island
    """

    peri = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                if (i <= 0 or grid[i - 1][j] == 0):
                    peri += 1
                if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                    peri += 1
                if (j <= 0 or grid[i][j - 1] == 0):
                    peri += 1
                if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    peri += 1
    return peri
