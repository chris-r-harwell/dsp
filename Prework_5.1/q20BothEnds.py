#!/bin/env python3

import os
import sys


# Complete the function below.


def both_ends(s):
    if len(s) < 2:
        return ''
    return s[0:2]+s[-2:]


s = sys.stdin.readline().strip()
res = both_ends(s)
print(res)
