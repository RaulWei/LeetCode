# -*- coding: UTF-8 -*-
__author__ = 'wang'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # :type inorder: List[int]
    # :type postorder: List[int]
    # :rtype: TreeNode
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        # 后序遍历的最后一个节点一定是根节点
        root_value = postorder.pop()
        root = TreeNode(root_value)
        i = inorder.index(root_value)
        # 递归构造右子树和左子树 注意应该是先构造右子树 保证postorder的最后一个节点是当前根节点
        root.right = self.buildTree(inorder[i+1:], postorder)
        root.left = self.buildTree(inorder[:i], postorder)
        return root

if __name__ == '__main__':
    sol = Solution()
    root = sol.buildTree([4, 2, 5, 1, 3], [4, 5, 2, 3, 1])
