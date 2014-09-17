#!/usr/bin/env python
#
# Topological sort
#
# TC: \Theta(|V|+|E|) --> if adjacent list is used
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.17
#

from graph_dfs import DFS


def topological_sort(G):
    G = DFS(G)
    L = [ (u[0],u[1]['f']) for u in G.nodes(data=True) ]
    L.sort(key=lambda x: -x[1])
    return [ x[0] for x in L ]
