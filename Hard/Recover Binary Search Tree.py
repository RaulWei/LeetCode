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
        res, count = [], 0
        self.recvTree(root, -1 * sys.maxint - 1, sys.maxint, res, root)
        return root

    def recvTree(self, root, left_val, right_val, res, r):
        if not root:
            return
        if left_val >= root.val or root.val >= right_val:
            res.append(root)
            if len(res) == 2:
                tmp = res[0].val
                res[0].val = res[1].val
                res[1].val = tmp
                return
        self.recvTree(root.left, left_val, root.val, res, r)
        self.recvTree(root.right, root.val, right_val, res, r)
        if len(res) == 1:
            tmp = r.val
            r.val = res[0].val
            res[0].val = tmp

    def swap(self, p1, p2):
        tmp = p1.val
        p1.val = p2.val
        p2.val = tmp


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

    p11 = TreeNode(0)
    p12 = TreeNode(1)
    p13 = TreeNode(-1)
    p11.left = p12
    p11.right = p13
    sol.swap(p12,p13)
    print(p12.val)
    print(p13.val)
    sol.recoverTree(p1)