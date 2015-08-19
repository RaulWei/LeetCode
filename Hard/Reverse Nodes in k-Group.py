# -*- coding: UTF-8 -*-
__author__ = 'weimw'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        cur = head
        count = 0
        while cur is not None and count < k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count > 0:
                next = head.next
                head.next = cur
                cur = head
                head = next
                count -= 1
            head = cur
        return head

if __name__ == '__main__':
    p1 = ListNode(1)
    sol = Solution()
    sol.reverseKGroup(p1, 1)
