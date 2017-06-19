#!/bin/env python3

"""
Weighted mean calculation

Given an array, X, of N integers and an array, W,
representing the respective weights of X's elements,
calculate and print the weighted mean of X's elements.
Your answer should be rounded to a scale of 1 decimal place.

INPUT: 3 lines
 int N num of ele in arrays X and W
 N space separated int in X
 N space separated int in W

Contraints:
     5 <= N <= 50
     0 < x_i <= 100, where x_i is the ith element of array X
     0 < w_i <= 100, where w_i is the ith element of array W

OUTPUT:
 weighted mean scale of 1 decimal place
"""


def get_weighted_mean(a, weights, count):
    total = 0

    for i in range(count):
        # print('item {} weight {} value {}'.format(i, weights[i], a[i]))
        total += weights[i]*a[i]

    return total/sum(weights)


def p1print(a):
    print("{:.1f}".format(round(a, 1)))


if __name__ == '__main__':
    n = int(input())
    X = list(map(int, input().split()))
    W = list(map(int, input().split()))
    p1print(get_weighted_mean(X, W, n))
