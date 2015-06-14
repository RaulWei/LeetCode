# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
归并两个有序链表
迭代算法
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
    def mergeTwoLists(self, l1, l2):
        if l1 is None and l2 is None:
            return None
        if l1 is None and l2 is not None:
            return l2
        if l1 is not None and l2 is None:
            return l1
        p1 = l1
        p2 = l2
        virt = ListNode(0)
        pre = virt
        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                virt.next = p1
                p1 = p1.next
            else:
                virt.next = p2
                p2 = p2.next
            virt = virt.next
        if p1 is None:
            virt.next = p2
        else:
            virt.next = p1
        return pre.next

if __name__ == '__main__':
    pa1 = ListNode(1)
    pa2 = ListNode(2)
    pa3 = ListNode(3)
    pb1 = ListNode(1)
    pb2 = ListNode(3)
    pa1.next = pa2
    pa2.next = pa3
    pb1.next = pb2

    sol = Solution()
    sol.mergeTwoLists(pa1, pb1)
