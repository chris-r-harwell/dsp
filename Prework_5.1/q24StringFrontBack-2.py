#!/bin/env python3

import os
import sys


def split_string(s):
    """
    INPUT: string
    OUTPUT: two strings
    split input in half with an extra char in front for those with an
    odd number of characters.

    """
    length = len(s)

    middle = length // 2
    if length % 2 != 0:
        middle += 1

    front = s[:middle]
    back = s[middle:]
    return front, back


def front_back(s1, s2):
    """
    INPUT: two strings
    OUTPUT: a-front + b-front + a-back + b-back
    where -front and -back are the strings split in half with
    an extra char in front for those with an odd number of characters.
    """
    a_front, a_back = split_string(s1)
    b_front, b_back = split_string(s2)

    return a_front + b_front + a_back + b_back


s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
res = front_back(s1, s2)
print(res)
