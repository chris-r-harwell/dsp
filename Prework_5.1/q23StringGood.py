#!/bin/env python3

import os
import sys

# Complete the function below.


def not_bad(s):
    """
    INPUT: string
    OUTPUT: 'not ... bad' replaced with 'good'
    """
    pos1 = s.find('not')
    pos2 = s.find('bad')
    if pos1 < pos2:
        return s[0:pos1] + 'good' + s[pos2+3:]
    return s


s = sys.stdin.readline().strip()
res = not_bad(s)
print(res)
