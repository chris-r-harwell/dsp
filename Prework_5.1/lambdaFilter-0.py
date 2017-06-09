#!/bin/env python3

import json
import os
import sys


# Complete the function below.

f = lambda my_list: [x for x in my_list if x % 2 == 0]
if '<lambda>' not in f.__name__:
    raise ValueError('Please write a lambda function')

my_list = json.loads(sys.stdin.readline())
for x in f(my_list):
    print(x)
