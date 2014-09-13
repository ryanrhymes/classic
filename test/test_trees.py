#!/usr/bin/env python
#
# This script is used for testing tree algorithms.
#
# Liang Wang @ University of Helsinki, Finland
# 2014.09.13
#

import os
import sys
import random

sys.path.append('../code')


def get_random_binary_tree():
    from binary_tree import BinaryTree, Node
    G = BinaryTree()
    G.root = Node(5)
    G.root.left = Node(2); G.root.right = Node(7)
    G.root.left.left = Node(1); G.root.left.right = Node(4)
    G.root.right.right = Node(8)
    return G


def main():

    G = get_random_binary_tree()
    print 'Test Binary Tree', '-'*20
    G.inorder_walk(G.root); print '';
    G.preorder_walk(G.root); print '';
    G.postorder_walk(G.root); print '';
    print G.search(4).value

    pass


if __name__ == "__main__":
    main()
    sys.exit(0)
