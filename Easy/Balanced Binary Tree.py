# -*- coding: UTF-8 -*-
__author__ = 'weimw'

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getDepth(self, root):
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        depth_left = self.getDepth(root.left)
        depth_right = self.getDepth(root.right)
        if depth_left < depth_right:
            return 1 + depth_right
        else:
            return 1 + depth_left

    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        if not root:
            return True
        depth_left = self.getDepth(root.left)
        depth_right = self.getDepth(root.right)
        if abs(depth_left - depth_right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    p1 = TreeNode(1)
    p2 = TreeNode(1)
    p3 = TreeNode(1)
    p1.left = p2
    p2.right = p3
    print(sol.isBalanced(p1))

