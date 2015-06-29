# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
题目要求此题时间复杂度为O(NlogN) 因此采用归并排序

思路：
设置两个指针，一个步长为1， 一个步长为2，当快指针到达尾结点时，慢指针指向中间结点，时间复杂度为O(N)；
平分为左链表L1和右链表L2，递归分裂，直到链表为空或者只有一个结点；
将链表L2的每个结点插入到链表L1中，时间复杂度为O(m+n)，m、n分别为两条链表的长度。
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
        virtual = ListNode('res')
        virtual.next = left
        pre = virtual
        # 合并两个已经排序的链表left和right
        while left and right:
            if left.val <= right.val:
                left = left.next
                pre = pre.next
            else:
                pre.next = right
                right = right.next
                pre = pre.next
                pre.next = left
        if not left:
            pre.next = right
        return virtual.next


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
    p1 = ListNode(2)
    p2 = ListNode(1)
    p3 = ListNode(4)
    p4 = ListNode(3)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p = sol.sortList(p1)
    p5 = ListNode(1)
