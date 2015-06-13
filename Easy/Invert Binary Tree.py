# -*- coding: UTF-8 -*-
__author__ = 'weimw'

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root is None or (root.left is None and root.right is None):
            return root
        else:
            t = root.right
            root.right = root.left
            root.left = t
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    sol.invertTree(root)
