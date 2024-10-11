#!/usr/bin/python3
"""
Represents the method to determine if all boxes can be opened
Using prototype: def canUnlockAll(boxes)
"""


def canUnlockAll(boxes):
    """
    Module that Checks if boxes can be unlocked
    """
    for Special_key in range(1, len(boxes) - 1):
        count = False
        for idx in range(len(boxes)):
            count = (Special_key in boxes[idx] and Special_key != idx)
            if count:
                break
        if count is False:
            return count
    return True
