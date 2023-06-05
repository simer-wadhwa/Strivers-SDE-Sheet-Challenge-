from math import *
from collections import *
from sys import *
from os import *

from typing import List


def setZeros(matrix: List[List[int]]) -> None:
    # Write your code here.
    temp = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                temp.append((i, j))

    for ind in temp:

        r = ind[0]
        c = ind[1]
        for i in range(len(matrix)):
            matrix[i][c] = 0

        for j in range(len(matrix[0])):
            matrix[r][j] = 0
