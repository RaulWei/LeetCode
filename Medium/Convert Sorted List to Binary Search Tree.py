# -*- coding: UTF-8 -*-
__author__ = 'wang'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # :type head: ListNode
    # :rtype: TreeNode
    def sortedListToBST(self, head):
        if not head:
            return None
        # 以链表中间节点为root 同时把原链表切分
        pre, slow, fast = None, head, head
        while fast.next and fast.next.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        if pre:
            pre.next = None
        else:
            head = pre
        root = TreeNode(slow.val)
        # 递归构造左子树和右子树
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root

if __name__ == '__main__':
    p1 = ListNode(3)
    p2 = ListNode(8)
    p3 = ListNode(9)
    p4 = ListNode(10)
    p5 = ListNode(13)
    p6 = ListNode(15)
    p7 = ListNode(16)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    p5.next = p6
    p6.next = p7
    sol = Solution()
    root = sol.sortedListToBST(p1)
    pass