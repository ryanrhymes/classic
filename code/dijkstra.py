#!/usr/bin/env python
#
# Dijkstra algorithm
#
# D algorithm is a greedy strategy
#
# TC: O(|V|^2)
# TC: O(|E|+|V|*lg|V|) --> min-priority queue implemented by a Fibonacci heap
# Edge weights are non-negative
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.12
#

def dijkstra(G, src):
    Q = {}     # Q = V \ S
    D = {}     # used for storing the current distance
    P = {}     # used for reconstructing shortest path
    
    for n in G.nodes():
        Q[n] = float('inf')
        D[n] = float('inf')
        P[n] = None

    Q[src] = 0; D[src] = 0

    # calculate the shortest path
    while len(Q):
        u, d = min(Q.items(), key=lambda x: x[1])
        if d == float('inf'):
            break
        for v in G.neighbors(u):
            d = D[u] + G[u][v]['weight']
            if d < D[v]:
                D[v] = d
                Q[v] = d
                P[v] = u
        Q.pop(u)

    return D, P


def construct(P, dst):
    # Reconstruct shortest path from P
    path = [dst]
    while P[dst] is not None:
        path.insert(0, P[dst])
        dst = P[dst]
    return path


def shortest(G, src, dst):
    D, P = dijkstra(G, src)
    return construct(P, dst)
