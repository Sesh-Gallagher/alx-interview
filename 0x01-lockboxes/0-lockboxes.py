#!/usr/bin/python3
"""
Module to determine if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Represent a function to check if boxes can be unlocked
    """
    for key in range(1, len(boxes) - 1):
        count = False
        for idx in range(len(boxes)):
            count = (key in boxes[idx] and key != idx)
            if count:
                break
        if count is False:
            return count
    return True
