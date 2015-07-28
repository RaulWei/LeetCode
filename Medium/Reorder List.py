# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
L1 - L2 - ... Ln-1 - Ln -> L1 - Ln - L2 - Ln-1 ...

1 找到串中心 把原串分隔 以h1,h2开头
2 后半串h2求逆
3 合并两串
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        if not head:
            return

        # splitList
        p1, p2 = head, head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
        h1, h2 = head, self.reverseList(p1.next)
        p1.next = None

        # mergeList
        r, h = h1, h1
        while h1 and h2:
            h1 = h1.next
            h.next = h2
            h = h.next

            h2 = h2.next
            h.next = h1
            h = h.next
            
        # return nothing
        head = r

    def reverseList(self, head):
        # 迭代法求逆 解决递归过深
        last, cur = None, head
        while cur:
            next = cur.next
            cur.next = last
            last = cur
            cur = next
        return last

if __name__ == '__main__':
    sol = Solution()
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    sol.reorderList(p1)