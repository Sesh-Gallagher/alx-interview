#!/usr/bin/python3
"""
Given that num = n,write a method that calculates
the fewest number of operations needed to result
in exactly n H characters in a file
"""


def minOperations(n):
    """
    Reprsents function def minOperations(n)
    Return: Integer
    """

    results = 0
    i = 2
    while n > 1:
        #Verify if the problem has been broken down evenly
        while n % i == 0:
            # if true add a small problmes to the result
            results += i
            n /= i
            # create small problem that will result in gettin n
        i += 1
    return results
