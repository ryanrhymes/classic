#!/usr/bin/env python
#
# Finite Automaton string matching algorithm
#
# Preprocess: \Theta(m*|Sigma|)
# Matching: \Theta(n)
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.17
#

import numpy as np


def finite_automaton(P, T):
    S = build_sigma(T)
    delta = build_delta_func(P, S)

    m, n = len(P), len(T)
    q = 0; idx = -1
    for i in xrange(n):
        q = delta[q, S.index(T[i])]
        if q == m:
            idx = i
            break
    return idx - m + 1


def build_delta_func(P, S):
    m, s = len(P), len(S)
    delta = np.zeros((m,s), dtype=int)
    for i in xrange(m):
        for j in xrange(s):
            a = S[j]
            k = min(m, i+1)
            while k>0 and P[:k] != P[:i][-k+1:] + a:
                k -= 1
            delta[i,j] = k
    return delta


def build_sigma(T):
    S = set([ x for x in T ])
    return sorted(S)
