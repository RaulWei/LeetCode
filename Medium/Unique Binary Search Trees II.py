# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
1. 根节点可以任取min ~ max (例如min  = 1, max = n)，假如取定为i。
2. 则left subtree由min ~ i-1组成，假设可以有L种可能。right subtree由i+1 ~ max组成，假设有R种可能。生成所有可能的left/right subtree。
3. 对于每个生成的left subtree/right subtree组合<T_left(p), T_right(q)>，p = 1...L，q = 1...R，添加上根节点i而组成一颗新树。
'''

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

    # 返回以begin begin+1 ... 到end为根的树
    def genTrees(self, begin, end):
        if begin > end:
            return [None]
        ret = []    # ret在递归函数内申请 不通过传参得到 这点值得高度注意
        for i in range(begin, end + 1):
            left_sub_tree = self.genTrees(begin, i - 1)    # 左子树集合
            right_sub_tree = self.genTrees(i + 1, end)     # 右子树集合
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