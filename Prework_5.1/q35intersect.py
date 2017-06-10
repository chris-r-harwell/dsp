#!/bin/python3

import os
import random
import sys
from datetime import datetime


def intersect_lists_1(list1, list2):
    return [i for i in list1 if i in list2]


def intersect_lists_2(list1, list2):
    s1 = frozenset(list1)
    s2 = frozenset(list2)
    return s1.intersection(s2)


def measure_time(f, *args):
    then = datetime.now()
    res = f(*args)
    now = datetime.now()
    return res, now-then

list1 = random.sample(range(10**6), 10000)
list2 = random.sample(range(10**6), 10000)
ans1, time1 = measure_time(intersect_lists_1, list1, list2)
ans2, time2 = measure_time(intersect_lists_2, list1, list2)
print('intersect_lists_1: {}'.format(time1))
print('intersect_lists_2: {}'.format(time2))
assert time2 < time1 / 100, 'the function can be faster'
assert set(ans1) == set(ans2), 'the function does not work correctly'
print(1)
