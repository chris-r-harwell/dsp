#!/bin/env python3

import os
import sys


# Complete the function below.


def front_back(s1, s2):
    """
    INPUT: two strings
    OUTPUT: a-front + b-front + a-back + b-back
    where -front and -back are the strings split in half with
    an extra char in front for those with an odd number of characters.
    """
    length_of_a = len(s1)
    length_of_b = len(s2)

    middle_of_a = length_of_a // 2
    if length_of_a % 2 != 0:
        middle_of_a += 1

    a_front = s1[:middle_of_a]
    a_back = s1[middle_of_a:]

    middle_of_b = length_of_b // 2
    if length_of_b % 2 != 0:
        middle_of_b += + 1

    b_front = s2[:middle_of_b]
    b_back = s2[middle_of_b:]

    return a_front + b_front + a_back + b_back


s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
res = front_back(s1, s2)
print(res)
