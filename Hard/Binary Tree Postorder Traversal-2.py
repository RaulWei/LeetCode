# -*- coding:UTF-8 -*-
__author__ = 'Wang'

'''
后序遍历二叉树
递归将右子树入栈
递归将左子树入栈
最后依次出栈
结合了栈与递归
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inStack(self, root, stack):
        if not root:
            return
        stack.append(root.val)
        self.inStack(root.right, stack)
        self.inStack(root.left, stack)

    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        if not root:
            return []
        res = []
        stack = []
        self.inStack(root, stack)
        while stack:
            res.append(stack.pop())
        return res
