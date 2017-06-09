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
    if list1[0] < list2[0]:
        for i in range(len(list1))

            if i 




 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.


list1 = json.loads(sys.stdin.readline())
list2 = json.loads(sys.stdin.readline())

def measure(f, *args):
    then = datetime.now()
    ans = f(*args)
    now = datetime.now()
    return now-then, ans
    
def sort_(list1, list2):
    return sorted(list1 + list2)

# sort_time, _ = measure(sort_, list1, list2)
merge_time, ans = measure(linear_merge, list1, list2)
# assert merge_time < sort_time / 2, 'Are you merging the two lists?'
for x in ans:
    print(x)
