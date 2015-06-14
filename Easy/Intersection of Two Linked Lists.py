# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
题目的意思两条链表只要一碰到val相等的就说明相交
这点我一开始不是这么理解 如果是这样情况简单的多

看了题解 解法真的巧妙
时间复杂度O(A+B)
A尾巴跟着B B尾巴跟着A 指针一次移动一步 遇到val相同就找到交点

1-3-5-7
              -9-11
        2-4

1-3-5-7-9-11-2-4-9
2-4-9-11-1-3-5-7-9
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        pa = headA
        pb = headB
        while pa.val != pb.val:
            if pa.next is None and pb.next is not None:
                pa = headB
                pb = pb.next
            elif pb.next is None and pa.next is not None:
                pb = headA
                pa = pa.next
            elif pa.next is not None and pb.next is not None:
                pa = pa.next
                pb = pb.next
            else:
                return None
        return pa

if __name__ == '__main__':
    p1 = ListNode(9)
    p2 = ListNode(11)

    pa1 = ListNode(1)
    pa2 = ListNode(3)
    pa3 = ListNode(5)
    pa4 = ListNode(7)

    pb1 = ListNode(2)
    pb2 = ListNode(4)

    p1.next = p2
    pa1.next = pa2
    pa2.next = pa3
    pa3.next = pa4
    pa4.next = p1
    pb1.next = pb2
    pb2.next = p1

    sol = Solution()
    print(sol.getIntersectionNode(pa1, pb1))

