from os import *
from sys import *
from collections import *
from math import *


def findDuplicate(arr: list, n: int):
    # Write your code here.
    # Returns an integer.
    slow = arr[0]
    fast = arr[0]

    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    slow = arr[0]

    while fast != slow:
        slow = arr[slow]
        fast = arr[fast]

    return slow