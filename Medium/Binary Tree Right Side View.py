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
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        pass

if __name__ == '__main__':
    sol = Solution()