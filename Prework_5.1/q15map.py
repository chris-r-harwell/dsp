#!/bin/env python3

import os
import sys


items_list = [1, 2, 3, 4, 5]


def sqr(x):
    return x ** 2


# Your answer should be one line. Use map.
items_squared = map(sqr, items_list)

with open('solution.py', 'r') as f:
    lines = f.readlines()[10:]
solution_line = [line for line in lines
                 if line.startswith('items_squared')]
solution_line = solution_line[0]

# assert not items_squared.count('\n'), 'string should be one line'
assert 'map' in solution_line, 'use "map"'
assert 'sqr' in solution_line, 'use the predefined function "sqr"'
assert 'items_list' in solution_line, \
       'use the predefined variable "items_list"'
for item in items_squared:
    print(item)
