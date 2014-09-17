#!/usr/bin/env python
#
# Rabin-Karp string matching algorithm
#
# Preprocess: \Theta(n)
# Matching average case  O(n)
# Matching worst case    O((n-m+1)*m)
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.17
#


def rabin_karp(P, T):
    m, n = len(P), len(T)
    p, t = 0, 0
    d, q = 10, 19
    h = d**(m-1) % q
    idx = -1

    for i in xrange(m):
        p = (d*p + int(P[i])) % q
        t = (d*t + int(T[i])) % q

    for j in xrange(n-m):
        if p == t and P == T[j:j+m]:
            idx = j
            break
        if j < (n - m):
            t = (d*(t - int(T[j])*h) + int(T[j+m])) % q

    return idx
