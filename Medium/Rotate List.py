# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
1->2->3, 20000000000
超过最大递归深度了
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if not head:
            return None
        if k == 0:
            return head
        virtual = ListNode(-1)
        pre, cur = virtual, head
        pre.next = head
        while cur.next:
            cur = cur.next
            pre = pre.next
        # 此时cur指向链表最后一个
        if cur != head:
            cur.next = head
            pre.next = None
        return self.rotateRight(cur, k-1)

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
    sol.rotateRight(p1, 2)
    pass
