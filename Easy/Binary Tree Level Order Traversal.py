# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
利用队列进行层序遍历二叉树
小变种 根据层级划分
'''

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
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
            res_t.append([t[0].val, t[1]])
        # 根据层级划分
        res = [[] for i in range(res_t[-1][1])]
        for i in range(len(res_t)):
            res[res_t[i][1] - 1].append(res_t[i][0])
        return res

if __name__ == '__main__':
    sol = Solution()
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    p5 = TreeNode(5)
    p1.left = p2
    p1.right = p3
    p3.left = p4
    p3.right = p5
    sol.levelOrder(p1)
