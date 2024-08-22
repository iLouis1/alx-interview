#!/usr/bin/python3
'''Given a pile of coins of different values,
    determines fewest number of coins needed to meet
    a given amount total.
'''
import sys


def makeChange(coins, total):
    '''
    Return: Fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    '''
    if total <= 0:
        return 0
    table = [sys.maxsize] * (total + 1)
    table[0] = 0
    m = len(coins)
    for k in range(1, total + 1):
        for v in range(m):
            if coins[v] <= k:
                subres = table[k - coins[v]]
                if subres != sys.maxsize and subres + 1 < table[k]:
                    table[k] = subres + 1

    if table[total] == sys.maxsize:
        return -1
    return table[total]
