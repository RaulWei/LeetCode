# -*- coding: UTF-8 -*-
__author__ = 'wang'

# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    hasCopyed = set()
    # :type node: UndirectedGraphNode
    # :rtype: UndirectedGraphNode
    def cloneGraph(self, node):
        if not node:
            return None
        if node.label not in self.hasCopyed:
            new_node = UndirectedGraphNode(node.label)
            self.hasCopyed.add(new_node.label)
            for n in node.neighbors:
                new_node.neighbors.append(self.cloneGraph(n))
            return new_node