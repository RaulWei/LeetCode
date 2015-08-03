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
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 切分为两段
        h1, h2 = head, self.reverseLink(slow.next)
        p1, p2 = h1, h2
        # 比较两段
        while p2:
            if p1.val != p2.val:
                return False
            p1, p2 = p1.next, p2.next
        return True

    def reverseLink(self, head):
        pre, next = None, head.next
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return head

if __name__ == '__main__':
    sol = Solution()
