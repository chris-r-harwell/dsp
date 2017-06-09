#!/bin/env python3

import os
import sys


# Complete the function below.

def mix_up(a, b):
    """
    INPUT: strings a and b of len >= 2
    OUTPUT: str with a and b sep by ' '
      AND swap first two char of ea. string.
    """
    return b[:2] + a[2:] + ' ' + a[:2] + b[2:]


a = sys.stdin.readline()
b = sys.stdin.readline()
a = a.rstrip('\n')
b = b.rstrip('\n')
print(mix_up(a, b))
