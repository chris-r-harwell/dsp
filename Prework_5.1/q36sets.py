#!/bin/python3

import os
import random
import sys
from datetime import datetime, timedelta

def remove_duplicates(somelist):
    return frozenset(somelist)


somelist = [random.randint(0, 10000) for i in range(1000)]
then = datetime.now()
ans = remove_duplicates(somelist)
now = datetime.now()
print('{}'.format(now - then))
assert (now-then) < timedelta(0, 0, 100), 'the function can be faster'
assert not len(ans) - len(set(ans)), 'there are dupes in your answer'
assert all(i in somelist for i in ans)

print(1)
