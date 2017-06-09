#!/bin/env python3

from datetime import datetime
import os
import sys


# Complete the function below.

DATE_FORMAT = '%m-%d-%Y'


def difference_in_days(date1, date2):
    dt1 = datetime.strptime(date1, DATE_FORMAT)
    dt2 = datetime.strptime(date2, DATE_FORMAT)
    delta = dt2 - dt1
    return delta.days


date1 = sys.stdin.readline().strip()
date2 = sys.stdin.readline().strip()
diff = difference_in_days(date1, date2)
print(diff)
