from os import *
from sys import *
from collections import *
from math import *


def nextPermutation(permutation, n):
    # Write your code here.
    # Return a list.
    i = n - 2
    j = n - 1
    while i >= 0 and permutation[i] >= permutation[i + 1]:
        i -= 1
    if i < 0:
        permutation.reverse()
        return permutation
    else:

        while permutation[j] <= permutation[i]:
            j -= 1

        permutation[i], permutation[j] = permutation[j], permutation[i]
        permutation[i + 1:] = reversed(permutation[i + 1:])

    return permutation


