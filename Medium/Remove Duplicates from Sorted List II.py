# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
三指针
c 当前指针
p 前一个指针
r 结果指针
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if head is None:
            return None
        virtual = ListNode('b')
        virtual.next = head
        p = virtual
        c = head
        r = ListNode('a')
        flag = True
        while p is not None:
            if c is None:
                if flag:
                    r.next = p
                    r = p
                else:
                    break
            elif c.val != p.val:
                if flag:
                    r.next = p
                    r = p
                else:
                    flag = True
            else:
                flag = False
            try:
                c = c.next
            except:
                break
            p = p.next
        r.next = None
        return virtual.next

if __name__ == '__main__':
    sol = Solution()
    p1 = ListNode(-1)
    p2 = ListNode(0)
    p3 = ListNode(0)
    p4 = ListNode(0)
    p5 = ListNode(0)
    p6 = ListNode(3)
    p7 = ListNode(3)

    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    p5.next = p6
    p6.next = p7

    sol.deleteDuplicates(p1)