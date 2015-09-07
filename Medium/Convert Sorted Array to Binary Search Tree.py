# -*- coding: UTF-8 -*-
__author__ = 'wang'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # :type nums: List[int]
    # :rtype: TreeNode
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        # 以nums中间的一个为root
        i = len(nums) / 2
        root = TreeNode(nums[i])
        # 递归构造左子树和右子树
        root.left = self.sortedArrayToBST(nums[:i])
        root.right = self.sortedArrayToBST(nums[i+1:])
        return root


if __name__ == '__main__':
    sol = Solution()
    root = sol.sortedArrayToBST([3, 8, 9, 10, 13, 15, 16])
