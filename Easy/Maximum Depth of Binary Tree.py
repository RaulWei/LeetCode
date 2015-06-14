# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
计算二叉树最大深度
简单递归
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if root is None:
            return 0
        depth_left = self.maxDepth(root.left)
        depth_right = self.maxDepth(root.right)
        if depth_left > depth_right:
            return 1 + depth_left
        return 1 + depth_right

if __name__ == '__main__':
    p1 = TreeNode(0)
    p2 = TreeNode(0)
    p3 = TreeNode(0)
    p4 = TreeNode(0)
    p5 = TreeNode(0)
    p1.left = p2
    p2.right = p3
    p3.left = p4
    p4.right = p5
    sol = Solution()
    print(sol.maxDepth(p1))
