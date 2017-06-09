#!/bin/env python3

import os
import sys


def sort_last(tuples_list):
    """
    INPUT: list of non-empty tuples
    OUTPUT: sorted list increasing order by last elementt in each tuple
    """
    new_list = sorted(tuples_list, key=lambda x: x[-1])
    return new_list


tuples = sys.stdin.read().split('\n')
tuples = map(eval, tuples)
res = sort_last(tuples)
for t in res:
    print(t)
