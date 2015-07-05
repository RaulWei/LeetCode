# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
实现二叉树结点的next指向
此方法只适合完美二叉树
'''

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        pre, cur = root, None
        while pre.left:
            cur = pre
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            pre = pre.left
        return

if __name__ == '__main__':
    sol = Solution()
    p1 = TreeLinkNode(1)
    p2 = TreeLinkNode(2)
    p3 = TreeLinkNode(3)
    p4 = TreeLinkNode(4)
    p5 = TreeLinkNode(5)
    p6 = TreeLinkNode(6)
    p7 = TreeLinkNode(7)
    p1.left = p2
    p1.right = p3
    p2.left = p4
    p2.right = p5
    p3.left = p6
    p3.right = p7
    sol.connect(p1)