#!/usr/bin/python3
""" this script shall determine fewest num of coins to make change"""


def makeChange(coins, total):
    """ THis function shall determine the fewest number of coins needed"""
    if (type(total) is not int) or type(coins) is not list:
        return -1
    if total <= 0:
        return 0
    try:
        less = [float('inf') for i in range(total + 1)]
        less[0] = 0
        for x in range(1, total + 1):
            for y in range(len(coins)):
                if less[x - coins[y]] + 1 < less[x]:
                    less[x] = less[x - coins[y]] + 1
        if less[total] != float('inf'):
            return less[total]
        else:
            return -1
    except Exception:
        return -1
