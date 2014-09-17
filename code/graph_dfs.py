#!/usr/bin/env python
#
# DFS algorithm
#
# D algorithm is a greedy strategy
#
# TC: \Theta(|V|+|E|) --> if adjacent list is used
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.17
#

import networkx as nx

time = 0


def DFS(G):
    # initialize
    for n in G.nodes(data=True):
        n[1]['c'] = 0
        n[1]['d'] = float('inf')
        n[1]['f'] = 0
        n[1]['p'] = None
    time = 0

    for n in G.nodes(data=True):
        if n[1]['c'] == 0:
            DFS_VISIT(G, n[0])
    return G


def DFS_VISIT(G, u):
    global time

    time += 1
    G.node[u]['d'] = time
    G.node[u]['c'] = 1
    
    for v in nx.neighbors(G, u):
        if G.node[v]['c'] == 0:
            G.node[v]['p'] = u
            DFS_VISIT(G, v)

    # access node and other operations
    time += 1
    G.node[u]['c'] = 2
    G.node[u]['f'] = time
    
    pass
