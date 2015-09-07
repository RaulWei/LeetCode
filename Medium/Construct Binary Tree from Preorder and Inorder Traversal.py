# -*- coding: UTF-8 -*-
__author__ = 'wang'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # :type preorder: List[int]
    # :type inorder: List[int]
    # :rtype: TreeNode
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        root, i = TreeNode(preorder[0]), 0
        while i < len(inorder) and inorder[i] != preorder[0]:
            i += 1
        root.left = self.buildTree(preorder[1:1+i], inorder[0:i])
        root.right = self.buildTree(preorder[1+i:], inorder[i+1:])
        return root

if __name__ == '__main__':
    sol = Solution()
    root = sol.buildTree([1, 2, 4, 5, 3], [4, 2, 5, 1, 3])
