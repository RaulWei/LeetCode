# -*- coding: UTF-8 -*-
__author__ = 'wang'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # :type root: TreeNode
    # :rtype: void Do not return anything, modify root in-place instead.
    def recoverTree(self, root):

    def recvTree(self, root, left_val, right_val):
        if not root:
            return
        if left_val < root.val < right_val and 

if __name__ == '__main__':
    sol = Solution()
    p1 = TreeNode(10)
    p2 = TreeNode(8)
    p3 = TreeNode(15)
    p4 = TreeNode(13)
    p5 = TreeNode(9)
    p6 = TreeNode(3)
    p7 = TreeNode(16)
    p1.left = p2
    p1.right = p3
    p2.left = p4
    p2.right = p5
    p3.left = p6
    p3.right = p7
    sol.recoverTree(p1)