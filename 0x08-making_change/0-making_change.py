#!/usr/bin/python3
"""
Make Change - Change comes from within
"""


def makeChange(coins, total):
    """
    Return the minimm number of coins needed to meet a given total
    Args: coins (list of ints): list of coins with different values
          totaal(int): minimum value to be met which is the totaol


    Return: Num of coins or -1 if meeting the set total is impossioble
    """
    if total <= 0:
        return 0
    coin_check = 0
    tempcoin = 0
    coins.sort(reverse=True)
    for i in coins:
        while coin_check < total:
            coin_check += i
            tempcoin += 1
        if coin_check == total:
            return tempcoin
        coin_check -= i
        tempcoin -= 1
    return -1
