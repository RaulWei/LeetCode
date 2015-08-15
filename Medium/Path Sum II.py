# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
深搜回溯
找出所有深搜路径中从root到leaf和为给定sum的路径
'''

import copy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.rest = []
        self.res = []

    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, sum):
        self.backtracking(root, sum)
        return self.res

    def backtracking(self, root, sum):
        if not root:
            return
        if not root.left and not root.right:
            # 叶子节点
            if sum == root.val:
                self.rest.append(root.val)
                res_t_cp = copy.deepcopy(self.rest)
                self.res.append(res_t_cp)
                self.rest.pop()
            return
        self.rest.append(root.val)
        self.pathSum(root.left, sum - root.val)
        self.pathSum(root.right, sum - root.val)
        self.rest.pop()

if __name__ == '__main__':
    p1 = TreeNode(5)
    p2 = TreeNode(4)
    p3 = TreeNode(8)
    p4 = TreeNode(11)
    p5 = TreeNode(13)
    p6 = TreeNode(4)
    p7 = TreeNode(7)
    p8 = TreeNode(2)
    p9 = TreeNode(5)
    p10 = TreeNode(1)
    p1.left = p2
    p1.right = p3
    p2.left = p4
    p3.left = p5
    p3.right = p6
    p4.left = p7
    p4.right = p8
    p6.left = p9
    p6.right = p10
    sol = Solution()
    sol.pathSum(p1, 22)

