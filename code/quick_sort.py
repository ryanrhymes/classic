#!/usr/bin/env python
#
# Quick sort algorithm
# time complexity is O(n*log(n))
# worst case is O(n^2)
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.11
#

def quick_sort(L, p, r):
    if p < r:
        q = partition(L, p, r)
        quick_sort(L, p, q - 1)
        quick_sort(L, q + 1, r)
    return L


def partition(L, p, r):
    i = p - 1
    for j in range(p, r):
        if L[i] < L[r]:
            i += 1
            
    pass
