#!/usr/bin/env python
#
# Radix sort algorithm
#
# LSD - Least Significant Digit
#
# TC: \Theta(d*n) where d is d-digit. Compared with comparison-based sort,
# which can do no better than O(n*lg(n)), Radix sort uses less passes, but
# each pass may take longer time.
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.13
#


def radix_sort(L, d):
    for i in range(1, d+1):
        L.sort(key = lambda x: str(x).zfill(d)[-i])
    return L


def sort(L):
    d = len(str(max(L)))
    radix_sort(L,d)
    return L
