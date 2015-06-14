# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
判断二叉树是否对称
参考 http://blog.csdn.net/ojshilu/article/details/14451907
另写一个isSym递归判断两棵树是否对称
isSym(left, right) and isSym(right, left) 参数传递的技巧
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # @param {TreeNode} rootA
    # @param {TreeNode} rootB
    # @param {boolean}
    def isSym(self, rootA, rootB):
        if rootA is None and rootB is None:
            return True
        elif (rootA is None and rootB is not None) or (rootA is not None and rootB is None):
            return False
        else:
            # rootA rootB都非空
            if rootA.val == rootB.val:
                return self.isSym(rootA.left, rootB.right) and self.isSym(rootA.right, rootB.left)
            else:
                return False

    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isSym(root.left, root.right)

if __name__ == '__main__':
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(2)
    p4 = TreeNode(3)
    p5 = TreeNode(1)
    p6 = TreeNode(1)
    p7 = TreeNode(4)
    p1.left = p2
    p1.right = p3
    p2.left = p4
    p2.right = p5
    p3.left = p6
    p3.right = p7

    sol = Solution()
    print(sol.isSymmetric(p1))