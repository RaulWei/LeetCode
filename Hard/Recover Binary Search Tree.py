# -*- coding: UTF-8 -*-
__author__ = 'wang'

import sys

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
        res = []
        self.recvTree(root, -1 * sys.maxint - 1, sys.maxint, res, 0)
        return root

    def recvTree(self, root, left_val, right_val, res, count):
        if not root:
            return
        if left_val >= root.val or root.val >= right_val:
            res.append(root)
            count += 1
            if count == 2:
                tmp = res[0].val
                res[0].val = res[1].val
                res[1].val = tmp
                return
        self.recvTree(root.left, left_val, root.val, res, count)
        self.recvTree(root.right, root.val, right_val, res, count)


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