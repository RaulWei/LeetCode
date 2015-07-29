# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
求任意二叉树中两个节点的最小祖先
递归解法
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            # 结束条件
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            # 两边都不空说明一左一右
            return root
        if left and not right:
            # p,q都在左边
            return left
        if not left and right:
            # P,q都在右边
            return right
