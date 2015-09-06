# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
利用一个性质 BST的中序遍历应该为有序序列
如何找错误的两节点 如序列 6 3 4 5 2
第一个错误节点为降序两点的前者 第二个错误节点为降序两点的后者
'''

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
        fst_wr_point, scd_wr_point = None, None
        pre = TreeNode(-1 * sys.maxint - 1)
        self.in_order_recvTree()

        # 交换两节点的值
        tmp = fst_wr_point.val
        fst_wr_point.val = scd_wr_point.val
        scd_wr_point.val = tmp

    def in_order_recvTree(self, root, pre):
        if not root:
            return

        self.in_order_recvTree(root.left, pre)
        # do
        self.in_order_recvTree(root.right, pre)



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
    print(p12.val)
    print(p13.val)
    sol.recoverTree(p1)