# -*- coding: UTF-8 -*-
__author__ = 'weimw'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if not head:
            return None
        virtual = ListNode('res')
        virtual.next, tail = head, head
        head = head.next
        tail.next = None
        while head:
            if head.val >= tail.val:
                tail.next = head
                head = head.next
                tail = tail.next
                tail.next  = None
                continue
            pre, cur = virtual, virtual.next
            while cur.val < head.val:
                cur = cur.next
                pre = pre.next
            t = head
            head = head.next
            pre.next = t
            t.next = cur
        return virtual.next

if __name__ == '__main__':
    sol = Solution()
    p1 = ListNode(4)
    p2 = ListNode(2)
    p3 = ListNode(1)
    p4 = ListNode(3)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    sol.insertionSortList(p1)