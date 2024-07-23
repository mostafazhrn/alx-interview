#!/usr/bin/python3
""" this script shall determine least num of coins needed to make change"""


def makeChange(coins, total):
    """ THis function shall determine fewest number of coins for mk chng"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    x = 0
    compt = 0
    coins_sum = len(coins)
    while compt < total and x < coins_sum:
        while coins[x] <= total - compt:
            compt += coins[x]
            count += 1
            if compt == total:
                return count
        x += 1
    return -1
