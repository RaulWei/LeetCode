# -*- coding: UTF-8 -*-
__author__ = 'weimw'

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if not self.root:
            return False
        return True

    # @return an integer, the next smallest number
    def next(self):
        res = self.root.val
        self.root = self.root.left
        return res

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())