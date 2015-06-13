# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
递归求链表的逆
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        t = head.next
        h = self.reverseList(head.next)
        # 尾巴其实不用这样求 以下求法超时 改为上上行
        # t = h
        # while t.next is not None:
        #     t = t.next
        t.next = head
        head.next = None
        return h

if __name__ == '__main__':
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p1.next = p2
    p2.next = p3

    sol = Solution()
    sol.reverseList(p1)

