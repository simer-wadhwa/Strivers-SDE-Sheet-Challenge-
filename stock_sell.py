from os import *
from sys import *
from collections import *
from math import *


def maximumProfit(prices):
    minele = maxsize
    maxele = -maxsize - 1
    for n in prices:
        minele = min(minele, n)
        maxele = max(maxele, n - minele)

    return maxele
