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
        ret = self.genTrees(1, n)
        return ret

    # 返回从begin到end为根的树的根节点集合
    def genTrees(self, begin, end):
        if begin > end:
            return [None]
        ret = []
        for i in range(begin, end + 1):
            left_sub_tree = self.genTrees(begin, i - 1)    # 左子树根节点集合
            right_sub_tree = self.genTrees(i + 1, end)     # 右子树根节点集合
            for left in left_sub_tree:
                for right in right_sub_tree:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    ret.append(root)
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.generateTrees(3))