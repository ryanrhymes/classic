#!/usr/bin/env python
#
# Knuth-Morris-Pratt string matching algorithm
#
# Preprocess: \Theta(m*|Sigma|)
# Matching: \Theta(n)
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.17
#


def KMP(P, T):
    prefunc = build_prefix_func(P)
    print P, prefunc
    return


def build_prefix_func(P):
    m, k = len(P), 0
    prefunc = [0]*m
    for i in xrange(1,m):
        while k > 0 and P[k] != P[i]:
            k = prefunc[k]
            print k
        if P[k] == P[i]:
            k += 1
        prefunc[i] = k
    return prefunc


