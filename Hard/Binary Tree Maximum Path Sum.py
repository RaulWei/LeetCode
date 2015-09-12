# -*- coding: UTF-8 -*-
__author__ = 'weimw'

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
        lrPathMax = root.val + max(self.maxPathDown(root.left), 0) + max(self.maxPathDown(root.right), 0)
        leftPathMax = self.maxPathSum(root.left)
        rightPathMax = self.maxPathSum(root.right)
        return max(lrPathMax, leftPathMax, rightPathMax)

    def maxPathDown(self, root):
        if not root:
            return 0
        maxLeftPathDown = self.maxPathDown(root.left)
        maxRightPathDown = self.maxPathDown(root.right)
        if maxLeftPathDown <= 0 and maxRightPathDown <= 0:
            return root.val
        if maxLeftPathDown > 0 and maxLeftPathDown >= maxRightPathDown:
            return root.val + maxLeftPathDown
        if maxRightPathDown > 0 and maxRightPathDown >= maxLeftPathDown:
            return root.val + maxRightPathDown

if __name__ == '__main__':
    sol = Solution()
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(-3)
    p1.left = p2
    p1.right = p3
    # sol.maxPathSum(p1)
    print(sol.maxPathSum(p4))
