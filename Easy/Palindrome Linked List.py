# -*- coding: UTF-8 -*-
__author__ = 'weimw'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if not head:
            return False
        # 找到中心点
        slow, fast = head, head
        
        pass

    def reverseLink(self, head):
        pre, next = None, head.next
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next

if __name__ == '__main__':
    sol = Solution()

