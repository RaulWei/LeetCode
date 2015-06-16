# -*- coding: UTF-8 -*-
__author__ = 'weimw'

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root, res):
        if not root:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        res = []
        self.inorder(root, res)
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
    print(sol.inorderTraversal(None))