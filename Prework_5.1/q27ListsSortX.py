#!/bin/env python3

import json
import os
import sys


def front_x(words):
    """
    INPUT: list of strings, lower case
    OUTPUT: sorted list
      except group all strings that begin with 'x' first.
    """
    x_words = [j for j in words if 'x' == j[0]]
    other_words = [j for j in words if 'x' != j[0]]
    return sorted(x_words) + sorted(other_words)

words = json.loads(sys.stdin.readline())
for w in front_x(words):
    print(w)
