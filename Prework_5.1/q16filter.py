#!/bin/env python3

import os
import sys


xlist = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 75, 100]

# Write your answer in one line, using "filter"
tens_list = filter(lambda a: a % 10 == 0, xlist)

with open('solution.py', 'r') as f:
    lines = f.readlines()[6:]
solution_line = [line for line in lines
                 if line.startswith('tens_list')]
solution_line = solution_line[0]

# assert not tens_list.count('\n'), 'your string needs to be one line'
assert 'filter' in solution_line, 'are you using "filter"?'
assert 'xlist' in solution_line, 'use the predefined variable "xlist"'
for i in tens_list:
    print(i)
