# -*- coding: UTF-8 -*-
__author__ = 'weimw'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # :type root: TreeNode
    # :rtype: bool
    def isValidBST(self, root):
        return self.checkBST(root, -1, 65535)

    def checkBST(self, root, left_val, right_val):
        # root为None
        if not root:
            return True
        # 没有左子树 也没有右子树
        if not root.left and not root.right:
            return True
        # 没有左子树 有右子树
        if not root.left:
            if right_val > root.val and self.checkBST(root.right, root.val, right_val):
                return True
            return False
        # 没有右子树 有左子树
        if not root.right:
            if left_val < root.val and self.checkBST(root.left, left_val, root.val):
                return True
            return False
        # 有左子树 有右子树
        if left_val < root.val < right_val and self.checkBST(root.left, left_val, root.val) and self.checkBST(root.right, root.val, right_val):
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p1.right = p2
    p2.right = p3
    print(sol.isValidBST(p1))