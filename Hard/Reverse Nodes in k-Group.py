# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
递归解法
reverseKGroup = 第一组reverse + reverseKGroup剩下的
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
    def reverseKGroup(self, head, k):
        cur = head
        count = 0
        while cur is not None and count < k:
            # 找Group
            cur = cur.next
            count += 1
        if count == k:
            # 找到Group 递归翻转剩余部分 手动翻转Group
            cur = self.reverseKGroup(cur, k)
            while count > 0:
                next = head.next
                head.next = cur
                cur = head
                head = next
                count -= 1
            head = cur
        return head

if __name__ == '__main__':
    p1 = ListNode(1)
    sol = Solution()
    sol.reverseKGroup(p1, 1)
