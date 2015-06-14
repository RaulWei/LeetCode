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
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        elif root.left is None and root.right is None:
            if sum == root.val:
                return True
            else:
                return False
        elif root.left is None and root.right is not None:
            return self.hasPathSum(root.right, sum-root.val)
        elif root.right is None and root.left is not None:
            return self.hasPathSum(root.left, sum-root.val)
        else:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

if __name__ == '__main__':
    p1 = TreeNode(5)
    p2 = TreeNode(4)
    p3 = TreeNode(8)
    p4 = TreeNode(11)
    p5 = TreeNode(13)
    p6 = TreeNode(4)
    p7 = TreeNode(7)
    p8 = TreeNode(2)
    p9 = TreeNode(1)
    p1.left = p2
    p1.right = p3
    p2.left = p4
    p3.left = p5
    p3.right = p6
    p4.left = p7
    p4.right = p8
    p6.right = p9

    sol = Solution()
    print(sol.hasPathSum(p9, 1))

