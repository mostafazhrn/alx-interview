#!/usr/bin/python3
""" this script shall contain the func for the prime game"""


def isWinner(x, nums):
    """ this func will determine the winner of the prime game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    arrnge = [True for _ in range(max(n + 1, 2))]
    for x in range(2, int(pow(n, 0.5) + 1)):
        if not arrnge[x]:
            continue
        for y in range(x * x, n + 1, x):
            arrnge[y] = False
    arrnge[0] = arrnge[1] = False
    a = 0
    for x in range(len(arrnge)):
        if arrnge[x]:
            a += 1
        arrnge[x] = a
    plyr = 0
    for n in nums:
        plyr += arrnge[n] % 2 == 1
    if plyr * 2 == len(nums):
        return None
    if plyr * 2 > len(nums):
        return "Maria"
    return "Ben"
