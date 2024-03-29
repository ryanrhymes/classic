#!/usr/bin/env python
#
# Heap sort algorithm
# 
# Comparison-based sorting algorithm
# In-place sorting
#
# TC: O(n*lg(n)), therefore combined good aspects of both 
# Insertion sort and Merge sort. Excellent but usually is
# beaten by Quick sort in practice.
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.13
#

import math


def heap_sort(L):
    build_max_heap(L)

    hSize = len(L)
    for i in xrange(hSize-1, 0, -1):
        L[0], L[i] = L[i], L[0]
        hSize -= 1
        max_heapify(L, 0, hSize)
    return L


def build_max_heap(L):
    # TC: linear time, O(n)
    for i in xrange(int(math.floor((len(L)-1)/2)), -1, -1):
        max_heapify(L, i, len(L))
    pass


def max_heapify(L, i, hSize):
    # TC: O(lg(n))
    l = left(i);  r = right(i); largest = i;
    
    if l < hSize and L[l] > L[i]:
        largest = l
    if r < hSize and L[r] > L[largest]:
        largest = r
    if i != largest:
        L[i], L[largest] = L[largest], L[i]
        max_heapify(L, largest, hSize)


def left(i): return 2*i+1
def right(i): return 2*i+2
def partent(i): return math.floor(i/2.0)


def sort(L):
    heap_sort(L)
    return L
