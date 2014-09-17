#!/usr/bin/env python
#
# BFS algorithm
#
# D algorithm is a greedy strategy
#
# TC: \Theta(|V|+|E|) --> if adjacent list is used
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.17
#

import networkx as nx


def BFS(G, s):
    # initialize
    for n in G.nodes(data=True):
        n[1]['color'] = 0
        n[1]['parent'] = None
        n[1]['distance'] = float('inf')

    G.node[s]['color']  = 1
    G.node[s]['parent'] = None
    G.node[s]['distance']  = 0

    Q = [s]
    while len(Q) != 0:
        u = Q.pop(0)
        # put more node into the queue
        for v in nx.neighbors(G,s):
            if G.node[v]['color'] == 0:
                G.node[v]['color'] = 1
                G.node[v]['parent'] = u
                G.node[v]['distance'] += 1
                Q.append(v)
        # color the node or other operations
        G.node[u]['color'] = 2
    return G
