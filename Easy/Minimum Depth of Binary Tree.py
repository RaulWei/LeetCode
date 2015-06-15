# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
计算二叉树最小深度
简单递归
比计算最大深度稍微复杂一点
分多种情况讨论
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        depth_left = self.minDepth(root.left)
        depth_right = self.minDepth(root.right)
        if depth_left == 0 and depth_right != 0:
            return 1 + depth_right
        elif depth_left != 0 and depth_right == 0:
            return 1 + depth_left
        elif depth_left == 0 and depth_right == 0:
            return 0
        else:
            if depth_left < depth_right:
                return 1 + depth_left
            return 1 + depth_right

if __name__ == '__main__':
    p1 = TreeNode(1)
    p2 = TreeNode(1)
    p3 = TreeNode(1)
    p4 = TreeNode(1)
    p5 = TreeNode(1)
    p6 = TreeNode(1)
    #p1.left = p2
    p1.right = p3
    p3.left = p4
    p4.right = p5
    p5.right = p6

    sol = Solution()
    print(sol.minDepth(None))
