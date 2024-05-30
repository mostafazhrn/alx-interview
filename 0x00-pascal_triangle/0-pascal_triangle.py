#!/usr/bin/python3
""" THis code shall return pascal triangle"""


def pascal_triangle(n):
    """ THis function shall return pascal triangle of n"""
    tri = []
    if n <= 0:
        return tri
    for i in range(n):
        row = [1]
        if tri:
            last_row = tri[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        tri.append(row)
    return tri
