# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
设计逆向前序 前序：中-左-右 逆向前序：中-右-左
递归的时候参数带上层数
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideOrder(self, root, res, level):
        if not root:
            return
        if len(res) < level:
            res.append(root.val)
        self.rightSideOrder(root.right, res, level + 1)
        self.rightSideOrder(root.left, res, level + 1)

    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        res = []
        self.rightSideOrder(root, res, 1)
        return res

if __name__ == '__main__':
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    p5 = TreeNode(5)
    p1.left = p2
    p1.right = p3
    p3.right = p4
    p2.right = p5

    sol = Solution()
    print(sol.rightSideView(p1))