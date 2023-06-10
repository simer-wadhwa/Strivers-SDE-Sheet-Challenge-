from math import *
from collections import *
from sys import *
from os import *


def majorityElementII(arr):
    # Write your code here.

    n = len(arr)
    count2 = 0
    count1 = 0
    ele1, ele2 = float('-inf'), float('-inf')
    for i in arr:
        if count1 == 0 and ele2 != i:
            count1 = 1
            ele1 = i

        elif count2 == 0 and ele1 != i:
            count2 = 1
            ele2 = i

        elif i == ele1:
            count1 += 1

        elif i == ele2:
            count2 += 1

        else:
            count1 -= 1
            count2 -= 1

    res = []

    temp1 = 0
    temp2 = 0
    for i in arr:
        if i == ele1:
            temp1 += 1
        if i == ele2:
            temp2 += 1

    mini = int(n // 3) + 1
    if (temp1 >= mini):
        res.append(ele1)
    if (temp2 >= mini):
        res.append(ele2)

    return res




