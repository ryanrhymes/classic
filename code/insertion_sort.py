#!/usr/bin/env python
#
# Insertion sort algorithm
#
# Comparion-based sorting algorithm
# In-place sorting
#
# best case time complexity is O(n)
# worst case time complexity is \Theta(n^2)
# in-place sorting 
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.12
#


def insertion_sort(L):
    for j in range(1, len(L)):
        t = L[j]
        i = j - 1
        while i >= 0 and L[i] > t:
            L[i+1] = L[i]
            i -= 1
        L[i+1] = t
    return L


def sort(L):
    insertion_sort(L)
    return L
