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
    S = [ str(x) for x in xrange(10) ]
    T = [ random.choice(S) for x in xrange(1000) ]
    T = ''.join(T)
    return (T, T[123:133])


def main():

    T, P = get_random_sample()
    from stringmatching_naive import naive
    print "Test Naive matching", naive, '-'*20
    print "The matching index =>", naive(P, T)

    from stringmatching_rabin_karp import rabin_karp
    print "Test Rabin-Karp matching", rabin_karp, '-'*20
    print "The matching index =>", rabin_karp(P, T)

    from stringmatching_finite_automaton import finite_automaton
    print "Test Finite Automaton matching", finite_automaton, '-'*20
    print "The matching index =>", finite_automaton(P, T)

    from stringmatching_kmp import KMP
    print "Test Knuth-Morris-Pratt matching", KMP, '-'*20
    print "The matching index =>", KMP(P, T)

    pass


if __name__ == "__main__":
    main()
    sys.exit(0)
