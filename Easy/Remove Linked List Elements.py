# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
技巧是在head前加一个虚拟指针
双指针 pre cur
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        virtual = ListNode(-1)
        virtual.next = head
        pre = virtual
        cur = head
        while cur:
            if cur.val == val:
                pre.next = cur.next
                cur = cur.next
            else:
                pre = pre.next
                cur = cur.next
        return virtual.next

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1)
    print(sol.removeElements(head, 2))
