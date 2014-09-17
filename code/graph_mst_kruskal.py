#!/usr/bin/env python
#
# Minimum spanning tree - Kruskal algorithm
#
# TC: \Theta(E*lgV)
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.17
#


def MST_KRUSKAL(G):
    T = set()
    D = dict()

    for n in G.nodes():
        D[n] = set([n])

    edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

    for edge in edges:
        u, v, _ = edge
        if (u not in D[v]) and (v not in D[u]):
            T.add((u,v))
            # union the two sets
            new_set = D[u] | D[v]
            D[u] = new_set; D[v] = new_set

    return T
