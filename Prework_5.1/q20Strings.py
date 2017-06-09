#!/bin/env python3

import os
import sys


# Complete the function below.

def fix_start(s):
    first_char = s[0]
    the_rest = s[1:]
    return first_char + the_rest.replace(first_char, '*')


s = sys.stdin.readline().rstrip('\n')
res = fix_start(s)
print(res)
