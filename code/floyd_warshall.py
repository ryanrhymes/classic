#!/usr/bin/env python
#
# Floyd-Warshall algorithm
#
# recursive form
# d(i,j,k+1) = min(d(i,j,k), d(i,k+1,k)+d(k+1,j,k))
#
# TC: \Theta(|V|^3)
# Edge weights are positive or negative, but no negative circles
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.12
#

import numpy


def floyd_warshall(G):
    N = len(G.nodes())
    D = numpy.full((N,N), float('inf'))
    P = numpy.full((N,N), float('inf'))

    # initialize
    for n in G.nodes():
        D[n,n] = 0
    for u, v in G.edges():
        D[u,v] = G[u][v]['weight']
        D[v,u] = D[u,v]

    # calculate all the shortest path
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if D[i,j] > D[i,k] + D[k,j]:
                    D[i,j] = D[i,k] + D[k,j]
                    P[i,j] = k
    return D, P


def construct(P, u, v):
    # Reconstruct shortest path
    k = P[u,v]
    if k == float('inf'):
        return []
    return construct(P,u,k) + [int(k)] + construct(P,k,v)


def shortest(G, src, dst):
    D, P = floyd_warshall(G)
    path = [src]+construct(P, src, dst)+[dst]
    return path
