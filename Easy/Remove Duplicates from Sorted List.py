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
    def deleteDuplicates(self, head):
        if head is None:
            return None
        i, j = head, head
        while i is not None:
            if i.val == j.val:
                i = i.next
            else:
                j.next = i
                j = i
                i = i.next
        j.next = None
        return head


if __name__ == '__main__':
    sol = Solution()
    p1 = ListNode(1)
    p2 = ListNode(1)
    p3 = ListNode(2)
    p4 = ListNode(3)
    p5 = ListNode(3)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    print(sol.deleteDuplicates(p5))
