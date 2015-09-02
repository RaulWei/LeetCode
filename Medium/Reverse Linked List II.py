# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
基本上算是模拟题 但往往leetcode上的模拟题我实现起来兼容边界条件比较费劲
把整条链表分为三段 第一段和第三段是正常顺序 第二段需要翻转
写代码时要充分考虑兼容第一段和第三段为空的情况
'''

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
        if not head:
            return head

        # 找到第一段的段尾 可能是空 可能是某个节点
        fst_lk_tail, p, i = None, head, 0
        while i < m - 1:
            fst_lk_tail = p
            p = p.next
            i += 1
        # 找到第三段的段头 它将作为翻转段的段尾的下一个
        rvs_lk_head, rvs_lk_pre = p, p
        while i < n:
            rvs_lk_pre = rvs_lk_pre.next
            i += 1

        # 开始翻转
        for i in range(n - m + 1):
            next = rvs_lk_head.next
            rvs_lk_head.next = rvs_lk_pre
            rvs_lk_pre = rvs_lk_head
            rvs_lk_head = next

        # 如果有第一段 则把第一段段尾连上翻转段段头 返回head
        # 如果没有第一段 则直接返回翻转段段头
        if fst_lk_tail:
            fst_lk_tail.next = rvs_lk_pre
        else:
            head = rvs_lk_pre
        return head

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
    sol.reverseBetween(p1, 1, 1)