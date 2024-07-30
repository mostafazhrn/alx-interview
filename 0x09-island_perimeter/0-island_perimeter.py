#!/usr/bin/python3
""" This script shall calculate the perimeter of an island in a grid"""


def island_perimeter(grid):
    """ This function calculates the perimeter of an island in a"""
    peri = 0
    for x in range(len(grid)):
        for i in range(len(grid[x])):
            if grid[x][i]:
                if i == 0 or not grid[x][i - 1]:
                    peri += 1
                if i == len(grid[x]) - 1 or not grid[x][i + 1]:
                    peri += 1
                if x == 0 or not grid[x - 1][i]:
                    peri += 1
                if x == len(grid) - 1 or not grid[x + 1][i]:
                    peri += 1
    return peri
