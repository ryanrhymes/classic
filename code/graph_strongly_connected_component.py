#!/usr/bin/env python
#
# Strongly connected component algorithm
#
#
# TC: \Theta(|V|+|E|) --> if adjacent list is used
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.17
#

import networkx as nx
from graph_dfs import DFS, DFS_VISIT


def SCC(G):
    G = DFS(G)
    L = [ (u[0],u[1]['f']) for u in G.nodes(data=True) ]
    L.sort(key=lambda x: -x[1])
    L = [ x[0] for x in L ]

    H = transpose(G)

    # DFS the G^T in decreasing finish time
    for n in H.nodes(data=True):
        n[1]['c'] = 0
        n[1]['d'] = float('inf')
        n[1]['f'] = 0
        n[1]['p'] = None
    time = 0

    for n in L:
        if H.node[n]['c'] == 0:
            DFS_VISIT(H, n)
    return H


def transpose(G):
    H = nx.DiGraph()
    for u, v in G.edges():
        H.add_edge(u,v)
    return H
