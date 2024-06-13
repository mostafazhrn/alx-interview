#!/usr/bin/python3
""" This script shall calc the min num of ops needed to copy all and paste"""


def minOperations(n):
    """ This instance shall calc min num of opes needed to copy all & paste"""
    if n < 2:
        return 0
    f_lst = []
    x = 1
    while n != 1:
        x += 1
        if n % x == 0:
            n = n / x
            f_lst.append(x)
            x = 1
    return sum(f_lst)
