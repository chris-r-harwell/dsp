#!/bin/env python3

import json
import os
import sys


def match_ends(s):
    """
    INPUT: list of strings
    OUTPUT: count of the number of strings where
     - len is 2 or more
    AND
     - 1st and last char of string are the same
    """
    count = 0
    for i in s:
        if len(i) >= 2:
            if i[0] == i[-1]:
                count += 1

    return count


s = json.loads(sys.stdin.readline())
print(match_ends(s))
