#!/bin/env python3


def get_median(a, n):
    """
    INPUT: sorted array, num elements
    OUTPUT: median, middle number if odd,
    average of middle two numbers if even.
    """
    mid = n // 2
    median = a[mid]
    if n % 2 == 0:
        mid -= 1
        median += a[mid]
        median /= 2

    return median


def get_mode(a):
    """
    INPUT: sorted array, num elements
    OUTPUT: smallest mode
    find the modes by
    first creating a dictionary
     - with keys from the unique values in the list
     - and values for the number of times they occur in the list
    find the maximum
    collect the modes with that maximum in a list
    and return the smallest element
    """
    modes = []
    b = dict.fromkeys(set(a), 1)
    for k in b.keys():
        b[k] = a.count(k)
    largest = max(b.values())
    for k, v in b.items():
        if v == largest:
            modes.append(k)
    modes.sort()
    mode = min(modes)
    return mode


def p1print(a):
    print("{:.1f}".format(round(a, 1)))


if __name__ == '__main__':
    n = int(input())
    array = sorted(list(map(int, input().split())))
    p1print(sum(array)/n)
    p1print(get_median(array, n))
    print(get_mode(array))
