#!/bin/env python3

import os
import sys


# Complete the function below.

def donuts(count):
    if count >= 10:
        count = 'many'
    return 'Number of donuts: {}'.format(str(count))


f = open(os.environ['OUTPUT_PATH'], 'w')
count = sys.stdin.readline()
count = int(count)
res = donuts(count)
f.write(res + "\n")

f.close()
