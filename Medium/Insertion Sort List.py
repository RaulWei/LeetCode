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
        while head:
            if head.val >= tail.val:
                tail.next = head
                tail = tail.next
                head = head.next
                continue
            pre, cur = virtual, virtual.next
            while cur.val < head.val:
                cur = cur.next
                pre = cur.next
            t = head
            head = head.next
            pre.next = t
            t.next = cur
        return virtual.next

if __name__ == '__main__':
    sol = Solution()
    p1 = ListNode(2)
    p2 = ListNode(1)
    p1.next = p2
    sol.insertionSortList(p1)