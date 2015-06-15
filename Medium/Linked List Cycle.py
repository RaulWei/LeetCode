# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
双指针判定链表是否有环
一个指针每次移动一次
一个指针每次移动两次
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head is None:
            return False
        p1, p2 = head, head
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
            if not p2:
                return False
            p2 = p2.next
            if p1 == p2:
                return True
        return False

if __name__ == '__main__':
    p1 = ListNode(1)
    p2 = ListNode(1)
    p3 = ListNode(1)
    p4 = ListNode(1)
    p5 = ListNode(1)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    p5.next = p2
    sol = Solution()
    print(sol.hasCycle(p1))
