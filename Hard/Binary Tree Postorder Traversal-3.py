# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
后序遍历二叉树
非递归
利用栈完成
非递归方法还是挺难想的 我也是看了别人的博客
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        stack = []
        res = []
        while root:
            # 从根节点开始 往左下走 全部入栈
            stack.append([root, 0])     # stack的数据[节点，该节点的右节点还没被访问过]
            root = root.left
        while stack:
            cur = stack[len(stack) - 1]
            if cur[1] == 1 or not cur[0].right:
                # 如果cur的右节点访问过或者没有右节点 说明可以访问cur了
                r = stack.pop()
                res.append(r[0].val)
            else:
                # 那么访问cur的右节点
                cur[1] = 1
                p = cur[0].right
                while p:
                    # 往左下走到尽头 一路入栈
                    stack.append([p, 0])
                    p = p.left
        return res

if __name__ == '__main__':
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    p5 = TreeNode(5)
    p1.left = p2
    p2.left = p3
    p3.right = p4
    p4.left = p5
    sol = Solution()
    print(sol.postorderTraversal(p1))