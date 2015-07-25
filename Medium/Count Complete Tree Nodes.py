# -*- coding: UTF-8 -*-
__author__ = 'weimw'

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if not root:
            return 0
        rLeft, rRight = root, root
        cLeft, cRight = 0, 0
        while rLeft:
            rLeft =  rLeft.left
            cLeft += 1
        while rRight:
            rRight = rRight.right
            cRight += 1
        if cLeft == cRight:
            return 2 ** cLeft - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

if __name__ == '__main__':
    p1 = TreeNode(1)
    sol = Solution()
    print(sol.countNodes(p1))
