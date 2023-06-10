from math import *
from collections import *
from sys import *
from os import *


def findMajorityElement(arr, n):
    # Write your code here.
    count = 0
    ele = -1
    for i in arr:
        if count == 0:
            count = 1
            ele = i

        elif i == ele:
            count += 1
        else:
            count -= 1

    temp = 0
    for i in arr:
        if i == ele:
            temp += 1

    if (temp > n / 2):
        return ele
    else:
        return -1




