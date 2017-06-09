#!/bin/env python3

import os
import sys


celsius = [39.2, 36.5, 37.3, 0, 20]
# write your answer in one line. use a list comprehension.
# use the variable "celsius"
# fahrenheit = [_*(212-32)/100 + 32.0 for _ in celsius]
fahrenheit = [_*(9/5) + 32.0 for _ in celsius]


with open('solution.py', 'r') as f:
    lines = f.readlines()[6:]
solution_line = [line for line in lines
                 if line.startswith('fahrenheit')]
solution_line = solution_line[0]

assert 'celsius' in solution_line, 'are you using a list comprehension?'
for i in fahrenheit:
    print(i)
