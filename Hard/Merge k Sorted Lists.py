# -*- coding: UTF-8 -*-
__author__ = 'weimw'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        if not lists:
            return None
        while len(lists) > 1:
            lists.append(self.mergeTwoLists(lists[0], lists[1]))
            lists.remove(lists[0])
            lists.remove(lists[0])
        return lists[0]

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
