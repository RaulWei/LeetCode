# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
从二叉搜索树中找到第k小
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def totalTreeNodeNum(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return 1 + self.totalTreeNodeNum(root.left) + self.totalTreeNodeNum(root.right)

    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        lChildNum = self.totalTreeNodeNum(root.left)
        if k <= lChildNum:
            # 第k小在左子树中找
            return self.kthSmallest(root.left, k)
        if lChildNum + 1 == k:
            # 第k小就是根节点
            return root.val
        if k > lChildNum + 1:
            # 第k小在右子树中找 更新k
            return self.kthSmallest(root.right, k - lChildNum - 1)

if __name__ == '__main__':
    sol = Solution()
    p1 = TreeNode(5)
    p2 = TreeNode(3)
    p3 = TreeNode(7)
    p4 = TreeNode(1)
    p5 = TreeNode(4)
    p6 = TreeNode(6)
    p7 = TreeNode(8)
    p1.left = p2
    p1.right = p3
    p2.left = p4
    p2.right = p5
    p3.left = p6
    p3.right = p7
    print(sol.kthSmallest(p1, 6))