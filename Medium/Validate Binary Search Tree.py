# -*- coding: UTF-8 -*-
__author__ = 'weimw'

import sys

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # :type root: TreeNode
    # :rtype: bool
    def isValidBST(self, root):
        return self.checkBST(root, -1 * sys.maxint - 1, sys.maxint)

    def checkBST(self, root, left_val, right_val):
        # root为None
        if not root:
            return True
        # 有左子树 有右子树
        if left_val < root.val < right_val and self.checkBST(root.left, left_val, root.val) and self.checkBST(root.right, root.val, right_val):
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    p1 = TreeNode(1)
    p2 = TreeNode(1)
    p3 = TreeNode(3)
    p1.right = p2
    # p2.right = p3
    print(sol.isValidBST(p1))