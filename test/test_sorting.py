#!/usr/bin/env python
#
# This script is used for testing sorting function.
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.12
#

import os
import sys
import random

sys.path.append('../code')


def get_random_numbers(n):
    return [ random.randint(0,n*10) for i in range(n) ]

def main():

    from quick_sort import sort
    print "Test quick_sort", sort, '-'*20
    L = get_random_numbers(10)
    print L
    print sort(L)

    from merge_sort import sort
    print "Test merge_sort", sort, '-'*20
    L = get_random_numbers(10)
    print L
    print sort(L)

    from insertion_sort import sort
    print "Test insertion_sort", sort, '-'*20
    L = get_random_numbers(10)
    print L
    print sort(L)

    pass


if __name__ == "__main__":
    main()
    sys.exit(0)
