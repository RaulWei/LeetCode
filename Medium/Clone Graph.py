# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
神奇啊 我以node作为dict的index就神奇的AC了 但是我以node.label作为dict就不行（本地可以） 蛋疼啊
'''

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
        if node not in self.hasCopyed:
            new_node = UndirectedGraphNode(node.label)
            self.hasCopyed[node] = new_node # 将node与new_node建立对应关系
            for n in node.neighbors:
                self.hasCopyed[node].neighbors.append(self.cloneGraph(n))
        # node不在dict中 处理到此可返回 hasCopyed[node]
        # node在dict中 直接返回 hasCopyed[node]
        return self.hasCopyed[node]


if __name__ == '__main__':
    p1 = UndirectedGraphNode(-1)
    p2 = UndirectedGraphNode(1)
    p1.neighbors.append(p1)
    p1.neighbors.append(p1)
    sol = Solution()
    p = sol.cloneGraph(p1)
