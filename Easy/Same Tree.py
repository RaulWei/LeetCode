# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
判断两棵树是否相同
递归的办法 有点慢
'''

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

if __name__ == '__main__':
    sol = Solution()
    t1 = TreeNode(0)
    t2 = TreeNode(1)
    print(sol.isSameTree(t1, t2))