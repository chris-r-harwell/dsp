#!/bin/env python3
"""
Task:
     Given an array, X, of n integers, calculate the respective first
     quartile(Q_1), second quartile(Q_2_, and third quartile(Q_3). It
     is guaranteed that Q_1, Q_2, and Q_3 are integers.

     Quartiles of an ordered data set are the 3 points that split the
     data set into 4 equal groups. The 3 quartiles are defined as follows:

     Q1: middle number between smallest number in a data set and its median
     Q2: median (50th percentile) of the data set.
     Q3: middle number between a data set's median and its largest number.


     IF n
       odd, do not include median (central value) in either half.
       even, split data set exactly in half.

INPUT: 2 lines
 n ele in array
 n space separated int in array X

Constraints:
    5 <= n <= 50
    0 < x_i <= 100, where x_i is the ith element of the array.

OUTPUT: 3 lines
    value of Q_1
    value of Q_2
    value of Q_3
"""


def get_median(a, n):
    """
    INPUT: sorted array, num elements
    OUTPUT: median, middle number if odd,
    average of middle two numbers if even.
    """
    # print('a = ' + repr(a))
    # print('n = ' + repr(n))
    assert len(a) == n
    mid = n // 2
    median = a[mid]
    if n % 2 == 0:
        mid -= 1
        median += a[mid]
        median /= 2

    return median


def get_quartiles(a, n):
    """
    INPUT: sorted array of ints a, num n
    OUTPUT: 1st, 2nd and 3rd quartiles
    """
    if n % 2 == 0:  # even
        m = n // 2
        q1 = get_median(a[0:m], m)
        q2 = get_median(a, n)
        q3 = get_median(a[m:], m)
    else:  # odd, exclude median
        m = n // 2
        q1 = get_median(a[0:m], m)
        q2 = get_median(a, n)
        q3 = get_median(a[m+1:], m)

    return (q1, q2, q3)


if __name__ == '__main__':
    n = int(input())
    X = sorted(list(map(int, input().split())))
    for i in get_quartiles(X, n):
        print(round(i))
