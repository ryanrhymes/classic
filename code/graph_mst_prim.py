#!/usr/bin/env python
#
# Minimum spanning tree - Prim algorithm
#
# TC: \Theta(E + V*lgV) --> if Fibonacci heap is used
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.17
#

import networkx as nx


def MST_PRIM(G, s):
    Q = dict()
    for n in G.nodes():
        Q[n] = float('inf')
    Q[s] = 0

    while len(Q) != 0:
        # Replace this one with Fibonacci heap
        # Then you can have O(lgV) TC
        u, w = min(Q.items(), key=lambda x: x[1])
        Q.pop(u)

        for v in nx.neighbors(G, u):
            if v in Q.keys() and G.edge[u][v]['weight'] < Q[v]:
                Q[v] = G.edge[u][v]['weight']
                G.node[v]['parent'] = u
    return (G, s)
