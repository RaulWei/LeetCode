# -*- coding: UTF-8 -*-
__author__ = 'weimw'

import sys

'''
maxPathDown(root)表示从root开始向下的单向path最大值
maxPathDown(root) =
    0, root = None
    root.val, maxPathDown(root.left) <=0 and maxPathDown(root.right) <= 0
    maxPathDown(root.left), maxPathDown(root.left) > 0 and maxPathDown(root.left) > maxPathDown(root.right)
    maxPathDown(root.right), maxPathDown(root.right) > 0 and maxPathDown(root.right) > maxPathDown(root.left)
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # :type root: TreeNode
    # :rtype: int
    def maxPathSum(self, root):
        if not root:
            return 0
        self.max_path_sum = -1 * sys.maxint - 1
        self.maxPathDown(root)
        return self.max_path_sum

    def maxPathDown(self, root):
        if not root:
            return 0
        maxLeftPathDown = max(self.maxPathDown(root.left), 0)
        maxRightPathDown = max(self.maxPathDown(root.right), 0)
        self.max_path_sum = max(maxLeftPathDown + maxRightPathDown + root.val, self.max_path_sum)
        return max(maxLeftPathDown, maxRightPathDown) + root.val


if __name__ == '__main__':
    sol = Solution()
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(-3)
    p1.left = p2
    p1.right = p3
    print(sol.maxPathSum(p1))
    print(sol.maxPathSum(p4))
