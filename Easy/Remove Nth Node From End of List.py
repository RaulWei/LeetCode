# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
双指针 fast指针比slow指针的起点快了n+1个
然后一起移动
当fast移到None的时候 slow就移到了倒数第n+1个
这样 slow.next = slow.next.next 即可
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        virtual = ListNode(0)
        virtual.next = head
        slow, fast = virtual, virtual
        for i in range(n + 1):
            # 将fast指针向前移动n+1个
            fast = fast.next
        while fast:
            # 双指针同时移动
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return virtual.next

if __name__ == '__main__':
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    sol = Solution()
    sol.removeNthFromEnd(p1, 2)
