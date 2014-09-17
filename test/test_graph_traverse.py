#!/usr/bin/env python
#
# This script is used for testing elementary graph algorithms.
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.17
#

import os
import sys
import random
import networkx as nx

sys.path.append('../code')


def get_random_graph():
    G = nx.erdos_renyi_graph(100, 0.1)
    return G


def main():

    G = get_random_graph()

    from graph_bfs import BFS
    print "Test graph BFS", BFS, '-'*20
    print 'Start with node id=5 =>', BFS(G, 5)

    from graph_dfs import DFS
    print "Test graph DFS", DFS, '-'*20
    print 'Start with node id=5 =>', DFS(G)

    from graph_toposort import topological_sort
    print "Test topological sort", topological_sort, '-'*20
    print 'Sorted list =>', topological_sort(G)

    from graph_strongly_connected_component import SCC
    print "Test SCC", SCC, '-'*20
    print 'SCC =>', SCC(G)

    pass


if __name__ == "__main__":
    main()
    sys.exit(0)
