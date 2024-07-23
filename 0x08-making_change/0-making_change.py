#!/usr/bin/python3
""" this script shall determine least num of coins needed to make change"""


def makeChange(coins, total):
    """ THis function shall determine fewest number of coins for mk chng"""
    if total <= 0:
        return 0
    if len(coins) == 0:
        return -1
    coins = sorted(coins)
    dyno = [float('inf')] * (total + 1)
    dyno[0] = 0
    for x in range(total + 1):
        for y in coins:
            if y > x:
                break
            if dyno[x - y] != -1:
                dyno[x] = min(dyno[x - y] + 1, dyno[x])
    if dyno[total] == float('inf'):
        return -1
    return dyno[total]
