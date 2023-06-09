from math import *
from collections import *
from sys import *
from os import *


def missingAndRepeating(arr, n):
    # Write your code here
    res = {}
    missing = -1
    repeat = -1
    for i in range(1, n + 1):
        res[i] = 0

    for i in arr:
        res[i] = res[i] + 1
        if res[i] > 1:
            repeat = i

    for i in range(1, n + 1):
        if res[i] == 0:
            missing = i
            break

    return missing, repeat