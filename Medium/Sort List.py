# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
题目要求此题时间复杂度为O(NlogN) 因此采用归并排序
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeSortedList(self, left, right):
        if not left:
            return right
        if not right:
            return left
        if left.val <= right.val:
            left.next = self.mergeSortedList(left.next, right)
            return left
        else:
            right.next = self.mergeSortedList(left, right.next)
            return right

    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if not head or not head.next:
            # 链表为空或只有一个节点
            return head

        # 把链表分为两部分
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        left, right = head, slow.next
        slow.next = None

        # 递归实现归并
        left = self.sortList(left)
        right = self.sortList(right)

        # 合并两个已经排序的链表
        return self.mergeSortedList(left, right)

if __name__ == '__main__':
    sol = Solution()
    
