# -*- coding: UTF-8 -*-
__author__ = 'weimw'

from collections import deque

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return []
        queue = deque([])
        level = 1
        queue.append([root, level])
        res_t = []
        while queue:
            t = queue.popleft()
            if t[0].left:
                queue.append([t[0].left, t[1] + 1])
            if t[0].right:
                queue.append([t[0].right, t[1] + 1])
            res_t.append([t[0], t[1]])
        # 根据队列里层序树节点构造next关系
        for i in range(1, len(res_t)):
            if res_t[i-1][1] == res_t[i][1]:
                res_t[i-1][0].next = res_t[i][0]
        return

if __name__ == '__main__':
    sol = Solution()
    p1 = TreeLinkNode(1)
    p2 = TreeLinkNode(2)
    p3 = TreeLinkNode(3)
    p4 = TreeLinkNode(4)
    p5 = TreeLinkNode(5)
    p6 = TreeLinkNode(6)
    p7 = TreeLinkNode(7)
    p1.left = p2
    p1.right = p3
    p2.left = p4
    p2.right = p5
    p3.left = p6
    p3.right = p7
    sol.connect(p1)