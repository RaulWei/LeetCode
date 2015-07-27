# -*- coding: UTF-8 -*-
__author__ = 'weimw'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        pass

    def reverseList(self, head):
        if not head:
            return None
        if not head.next:
            return head
        t = head.next
        h = self.reverseList(head.next)
        t.next = head
        head.next = None
        return h
