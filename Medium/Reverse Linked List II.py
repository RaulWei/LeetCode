# -*- coding: UTF-8 -*-
__author__ = 'wang'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # :type head: ListNode
    # :type m: int
    # :type n: int
    # :rtype: ListNode
    def reverseBetween(self, head, m, n):
        fst_lk_tail, i = head, 0
        while i < m - 1:
            fst_lk_tail = fst_lk_tail.next
            i += 1

        rvs_lk_head, rvs_lk_pre = fst_lk_tail.next, fst_lk_tail.next
        while i < n:
            rvs_lk_pre = rvs_lk_pre.next
            i += 1

        # 开始翻转
        for i in range(n - m):
            next = rvs_lk_head.next
            rvs_lk_head.next = rvs_lk_pre
            rvs_lk_pre = rvs_lk_head
            rvs_lk_head = next
        fst_lk_tail.next = rvs_lk_head

if __name__ == "__main__":
    sol = Solution()
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    sol.reverseBetween(p1, 2, 4)