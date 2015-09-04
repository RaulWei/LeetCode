# -*- coding: UTF-8 -*-
__author__ = 'weimw'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # :type n: int
    # :rtype: List[TreeNode]
    def generateTrees(self, n):
        pass

    def generateTreesByNode(self, b, n, res):
        if b == n:
            return

        for i in range(1, n + 1):
            res.append(i)
            self.generateTreesByNode(b, i - 1, res)
            self.generateTreesByNode(i + 1, n, res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateTrees(3))