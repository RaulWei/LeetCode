# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
两条链表 每条表示一个数的逆序 如1234表示4321
模拟求和
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        carry = 0
        p1 = l1
        p2 = l2
        pre = ListNode(0)
        pre.next = p1
        while p1 and p2:
            # p1 p2的公共部分
            curSum = p1.val + p2.val + carry
            p1.val = curSum % 10
            carry = curSum / 10
            p1 = p1.next
            p2 = p2.next
            pre = pre.next
        while p1:
            # p1比p2长
            curSum = p1.val + carry
            p1.val = curSum % 10
            carry = curSum / 10
            p1 = p1.next
            pre = pre.next
        if p2:
            # p2比p1长
            pre.next = p2
            while p2:
                curSum = p2.val + carry
                p2.val = curSum % 10
                carry = curSum / 10
                p2 = p2.next
                pre = pre.next
        if carry > 0:
            # 最后如果有进位要补上去
            pre.next = ListNode(carry)
        return l1

if __name__ == '__main__':
    pa1 = ListNode(9)
    pa2 = ListNode(8)
    pa3 = ListNode(9)
    pb1 = ListNode(1)
    pb2 = ListNode(9)
    pb3 = ListNode(9)
    pb4 = ListNode(9)
    pa1.next = pa2
    pa2.next = pa3
    pb1.next = pb2
    pb2.next = pb3
    pb3.next = pb4
    sol = Solution()
    sol.addTwoNumbers(pa1, pb1)
