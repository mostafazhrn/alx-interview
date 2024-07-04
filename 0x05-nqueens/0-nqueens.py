#!/usr/bin/python3
""" THis script shall solve the N queens problem"""
import sys


def resoudre(rw , col):
    """ This instance shall solve the N queens problem"""
    re_resoudre = [[]]
    for queen in range(rw):
        re_resoudre = q_plc(queen, col, re_resoudre)
    return re_resoudre


def q_plc(queen, col, prob_resoudre):
    """ This instance shall solve the N queens problem"""
    reso_queen = []
    for arr in prob_resoudre:
        for i in range(col):
            if is_right(queen, i, arr):
                reso_queen.append(arr + [i])
    return reso_queen

def is_right(queen, i, arr):
    """ This instance shall solve the N queens problem"""
    if i in arr:
        return False
    else:
        return all(abs(arr[col] - i) != queen - col for col in range(queen))
    

def main():
    """ this instance shall start the N queens solving"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        the_q = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if the_q < 4:
        print("N must be at least 4")
        sys.exit(1)
    return the_q

def n_queens():
    """ This instance shall solve the N queens problem"""
    the_q = main()
    re_resoudre = resoudre(the_q, the_q)
    for arr in re_resoudre:
        cle = []
        for i, col in enumerate(arr):
            cle.append([i, col])
        print(cle)


if __name__ == "__main__":
    n_queens()
