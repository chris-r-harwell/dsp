#!/bin/env python3

import os
import sys


# Complete the function below.

def verbing(s):
    """
    INPUT: String, lower case.
    OUTPUT: If str at least 3 long 'ing' added to end,
        unless it already ends in 'ing,
        in which case 'ly' added to end instead.
        If string len is less than 3 unchanged.
    """

    if len(s) < 3:
        return s

    if s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'ing'


s = input()
res = verbing(s)
print(res)
