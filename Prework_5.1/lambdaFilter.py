#!/bin/env python3

import json
import os
import sys


# Complete the function below.

def f(my_list):
    return [x for x in my_list if x % 2 == 0]

my_list = json.loads(sys.stdin.readline())
for x in f(my_list):
    print(x)
