# -*- coding:UTF-8 -*-

'''
后序遍历二叉树
递归解法和前序遍历以及中序遍历都差不多
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def post(self, root, res):
        if not root:
            return
        self.post(root.left, res)
        self.post(root.right, res)
        res.append(root.val)
        
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        res = []
        self.post(root, res)
        return res