from math import *
from collections import *
from sys import *
from os import *


def rotateMatrix(mat, n, m):
    # Write your code here

    for r in range(n):
        for c in range(m):
            mat[r][c] = mat[c][r]

    for row in mat:
        row.reverse()
