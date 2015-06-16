# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
递归前序遍历二叉树
依旧需要注意参数传递
自己写一个递归函数嵌套在给定的函数中
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorder(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)

    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        res = []
        self.preorder(root, res)
        return res

if __name__ == '__main__':
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    p5 = TreeNode(5)
    p1.left = p2
    p1.right = p3
    p2.left = p4
    p2.right = p5
    sol = Solution()
    print(sol.preorderTraversal(None))
