#!/usr/bin/env python
#
# Merge sort algorithm
# time complexity is \Theta(n*lg(n))
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.12
#


import math


def merge_sort(L, p, r):
    if p < r:
        q = int(math.floor( (p+r)/2.0 ))
        merge_sort(L, p, q)
        merge_sort(L, q+1, r)
        merge(L, p, q, r)
    pass


def merge(L, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L1, L2 = L[p:q+1], L[q+1:r+1]
    L1.append(float('inf'))
    L2.append(float('inf'))

    i, j = 0, 0
    for k in range(p, r+1):
        if L1[i] <= L2[j]:
            L[k] = L1[i]
            i += 1
        else:
            L[k] = L2[j]
            j += 1
    pass


def sort(L):
    merge_sort(L, 0, len(L)-1)
    return L
