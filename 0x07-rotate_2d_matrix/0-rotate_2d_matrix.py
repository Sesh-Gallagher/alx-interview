#!/usr/bin/python3
"""
Module to define a function that rotates
2D matrix 90 degrees clockwise in-place
"""


def rotate_2d_matrix(matrix):
    """
    RModule that rotate a 2d square matrix 90 degrees clockwise in-place
    Args:matrix (list): 2d square matrix
    Return: None
    """
    n = len(matrix)
    for a in range(n):
        for b in range(a):
            temp = matrix[a][b]
            matrix[a][b] = matrix[b][a]
            matrix[b][a] = temp

    for a in range(n):
        for b in range(int(n / 2)):
            temp = matrix[a][b]
            matrix[a][b] = matrix[a][n-1-b]
            matrix[a][n-1-b] = temp
