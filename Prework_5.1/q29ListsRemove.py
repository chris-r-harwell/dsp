#!/bin/env python3

import json
import os
import sys


def remove_adjacent(n):
    """
    INPUT: list of numbers
    OUTPUT: list of numbers,
      where adjacent equal elements reduced to a single element
    """
    last = ''
    new_list = []
    for i in n:
        if i == last:
            continue
        else:
            last = i
            new_list.append(i)

    return new_list


nums = json.loads(sys.stdin.readline())
for n in remove_adjacent(nums):
    print(n)
