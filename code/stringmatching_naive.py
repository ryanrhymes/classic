#!/usr/bin/env python
#
# Naive string matching algorithm
#
# Preprocess: 0
# Matching:   O((n-m+1)*m)
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.17
#


def naive(P, T):
    m, n = len(P), len(T)
    idx = -1
    for i in xrange(n-m):
        if P == T[i:i+m]:
            idx = i
            break

    return idx
