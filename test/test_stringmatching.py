#!/usr/bin/env python
#
# This script is used for testing string matching function.
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.17
#

import os
import sys
import random
import string

sys.path.append('../code')


def get_random_sample():
    T = [ random.choice(string.letters[0:26]) for x in xrange(1000) ]
    T = ''.join(T)
    return (T, T[123:133])

def main():

    T, P = get_random_sample()

    from stringmatching_naive import naive
    print "Test Naive matching", naive, '-'*20
    print naive(P, T)

    pass


if __name__ == "__main__":
    main()
    sys.exit(0)
