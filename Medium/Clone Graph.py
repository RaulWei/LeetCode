# -*- coding: UTF-8 -*-
__author__ = 'wang'

# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    hasCopyed = dict()
    # :type node: UndirectedGraphNode
    # :rtype: UndirectedGraphNode
    def cloneGraph(self, node):
        if not node:
            return node
        if node.label not in self.hasCopyed:
            new_node = UndirectedGraphNode(node.label)
            self.hasCopyed[new_node.label] = new_node
            for n in node.neighbors:
                self.hasCopyed[new_node.label].neighbors.append(self.cloneGraph(n))
            return self.hasCopyed[new_node.label]
        else:
            return self.hasCopyed[node.label]


if __name__ == '__main__':
    p1 = UndirectedGraphNode(-1)
    p2 = UndirectedGraphNode(1)
    p1.neighbors.append(p2)
    sol = Solution()
    p = sol.cloneGraph(p1)
    pass