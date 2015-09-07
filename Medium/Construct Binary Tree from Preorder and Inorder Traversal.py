# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
第一次碰到MLE 内存超过限制了
通过Discuss上了解到是切片做多了 为了减少切片我把preorder改为动态出栈而不是每次取它的第一个 递归时找“第一个”的位置
动态出栈后递归时就不用对preorder做切片 如下代码所示
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # :type preorder: List[int]
    # :type inorder: List[int]
    # :rtype: TreeNode
    def buildTree(self, preorder, inorder):
        if not len(preorder) or not len(inorder):
            return None
        root_value = preorder.pop(0)
        root = TreeNode(root_value)
        i = inorder.index(root_value)
        root.left = self.buildTree(preorder, inorder[0:i])  # 构建左子树 返回左子树root
        root.right = self.buildTree(preorder, inorder[i+1:])    # 构建右子树 返回右子树root
        return root

if __name__ == '__main__':
    sol = Solution()
    root = sol.buildTree([1, 2, 4, 5, 3], [4, 2, 5, 1, 3])
