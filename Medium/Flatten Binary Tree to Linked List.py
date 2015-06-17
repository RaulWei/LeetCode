# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
改变树的结构
         1
        / \
       2   5
      / \   \
     3   4   6

变成

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

实际上转换之后的树 每个节点的右孩子是该节点在原树先序遍历的下个节点
改改原来的先序遍历代码就可以过了
由于题目要求in-place 我把节点直接塞进res
最后遍历res 重新分配节点指向
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorder(self, root, res):
        if not root:
            return
        res.append(root)
        self.preorder(root.left, res)
        self.preorder(root.right, res)

    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        res = []
        self.preorder(root, res)
        if res:
            for i in range(len(res) - 1):
                res[i].right = res[i+1]
                res[i].left = None

if __name__ == '__main__':
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    p5 = TreeNode(5)
    p6 = TreeNode(6)
    p1.left = p2
    p1.right = p5
    p2.left = p3
    p2.right = p4
    p5.right = p6
    sol = Solution()
    sol.flatten(p1)
