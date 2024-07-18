#!/usr/bin/python3
""" This script shall rotate a 2D matrix 90 degrees clockwise. """


def rotate_2d_matrix(matrix):
    """ This function shall rotate a 2D matrix 90 degrees clockwise. """
    Mat = len(matrix)
    cop_mat = []
    rw_copy = 0
    for col in range(Mat):
        cop_mat.append([])
        for rw in range(Mat):
            cop_mat[rw_copy].append(matrix[rw][col])
        rw_copy += 1
    for rw in range(Mat):
        matrix[rw] = cop_mat[rw][::-1]
    return matrix
