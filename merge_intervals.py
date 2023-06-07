from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit


class Solution:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def mergeIntervals(intervals):
    # Write your code here.
    #intervals.sort()
    intervals.sort(key=lambda x: x.start)  # Sort intervals based on start value

    # Print the intervals before merging
    print("Intervals before merging:")
    for interval in intervals:
        print(interval.start, interval.end)
        merged=[intervals[0]]
    for interval in intervals[1:]:
        if merged[-1].end<interval.start:
            merged[-1].end=max(merged[-1].end,interval.end)
        else:
            merged.append(interval)
    return merged






n = int(input())
arr1 = list(map(int, stdin.readline().strip().split(" ")))
arr2 = list(map(int, stdin.readline().strip().split(" ")))
arr1.sort()
arr2.sort()
intervals = []
for i in range(n):
    a = Solution(arr1[i], arr2[i])
    print(type(a))
    print(a.start,a.end)
    intervals.append(a)

res = mergeIntervals(intervals)

for i in range(len(res)):
    print(res[i].start, res[i].end)
