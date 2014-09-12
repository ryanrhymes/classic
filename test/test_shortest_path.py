#!/usr/bin/env python
#
# This script is used for testing shortest path algorithm.
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.12
#

import os
import sys
import random
import networkx as nx

sys.path.append('../code')


def get_random_graph():
    G = nx.erdos_renyi_graph(100, 0.1)
    H = nx.Graph()
    for u,v in G.edges():
        d = random.uniform(1,10)
        H.add_edge(u, v, weight=d)
    return H


def main():

    G = get_random_graph()
    from dijkstra import shortest
    print "Test Dijkstra", shortest, '-'*20
    print 'NetworkX =>', nx.shortest_path(G, 0, 50, 'weight')
    print 'Dijkstra =>', shortest(G, 0, 50)
    pass


if __name__ == "__main__":
    main()
    sys.exit(0)
