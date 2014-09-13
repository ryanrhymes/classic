#!/usr/bin/env python
#
# Different tree algorithms
# 
# Liang Wang @ University of Helsinki, Finland
# 2014.09.13
#

import sys


class Node():
    left  = None
    right = None
    value = None

    def __init__(self, v=None):
        self.value = v
    pass


class BinaryTree():
    root = None

    def search(self, key):
        node = self.root
        while node != None and node.value != key:
            if key < node.value:
                node = node.left
            else:
                node = node.right
        return node

    def inorder_walk(self, node):
        if node is not None:
            self.inorder_walk(node.left)
            sys.stdout.write("%i " % node.value)
            self.inorder_walk(node.right)


    def preorder_walk(self, node):
        if node is not None:
            sys.stdout.write("%i " % node.value)
            self.inorder_walk(node.left)
            self.inorder_walk(node.right)


    def postorder_walk(self, node):
        if node is not None:
            self.inorder_walk(node.left)
            self.inorder_walk(node.right)
            sys.stdout.write("%i " % node.value)

    pass
