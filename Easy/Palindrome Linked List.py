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
        if not head or not head.next:
            return True
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
        return pre

if __name__ == '__main__':
    p1 = ListNode(1)
    p2 = ListNode(1)
    p3 = ListNode(2)
    p4 = ListNode(1)
    p5 = ListNode(1)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    sol = Solution()
    print(sol.isPalindrome(p1))
