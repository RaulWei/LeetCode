# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
什么是BST
1) 左子树的值都比根节点小；2) 右子树的值都比根节点大；3) 左右子树也必须满足上面两个条件。
需要注意的是，左子树的所有节点都要比根节点小，而非只是其左孩子比其小，右子树同样。
这是很容易出错的一点是，很多人往往只考虑了每个根节点比其左孩子大比其右孩子小。
例如 [5, 4, 10, #, #, 3, 11] 就不是BST

本题的巧妙在于递归时传入两个参数，一个左界，一个右界，节点值必须在左右界之间，递归时再更新左右界
'''

import sys

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
        return self.checkBST(root, -1 * sys.maxint - 1, sys.maxint)

    def checkBST(self, root, left_val, right_val):
        # root为None
        if not root:
            return True
        # 有左子树 有右子树 (左右子树可为None)
        if left_val < root.val < right_val and self.checkBST(root.left, left_val, root.val) and self.checkBST(root.right, root.val, right_val):
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    p1 = TreeNode(1)
    p2 = TreeNode(1)
    p3 = TreeNode(3)
    p1.right = p2
    p2.right = p3
    print(sol.isValidBST(p1))