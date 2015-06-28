# -*- coding: UTF-8 -*-
__author__ = 'weimw'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None:
            return None
        p1, p2 = head, head
        p = None
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
            if not p2:
                return None
            p2 = p2.next
            if p1 == p2:
                p = p1
                break
        p1, p2 = head, p
        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None

if __name__ == '__main__':
    sol = Solution()
    p1 = ListNode(1)
    p2 = ListNode(2)
    p1.next = p2
    p2.next = p1
    sol.detectCycle(p1)