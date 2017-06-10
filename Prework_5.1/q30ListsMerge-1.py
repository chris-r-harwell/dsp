#!/bin/env python3

from datetime import datetime
import json
import os
import sys


def linear_merge(list1, list2):
    """
    INPUT: two lists sorted in increasing order
    OUTPUT: merged list of all elements in sorted order
    """
    idx = 0
    while(len(list1)):
        if list1[0] <= list2[idx]:
            list2.insert(idx, list1.pop(0))
        else:
            idx += 1
    return list2


list1 = json.loads(sys.stdin.readline())
list2 = json.loads(sys.stdin.readline())


def measure(f, *args):
    then = datetime.now()
    ans = f(*args)
    now = datetime.now()
    return now-then, ans


def sort_(list1, list2):
    return sorted(list1 + list2)

sort_time, _ = measure(sort_, list1, list2)
merge_time, ans = measure(linear_merge, list1, list2)
print('sort_time = {}'.format(sort_time))
print('merge_time = {}'.format(merge_time))
assert merge_time < sort_time / 2, 'Are you merging the two lists?'

for x in ans:
    print(x)
