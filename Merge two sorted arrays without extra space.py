from math import *
from collections import *
from sys import *
from os import *


def ninjaAndSortedArrays(arr1, arr2, m, n):
    # Write your code here.
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1

    return arr1
