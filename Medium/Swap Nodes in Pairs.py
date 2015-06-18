# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
1-2-3-4 一对一对交换 变成 2-1-4-3
实际上可以递归实现 只需要把"一对"看成一个整体
swapPairs(1-2-3-4-5-6) = 2-1-swapPairs(3-4-5-6)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        pass

if __name__ == '__main__':
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)

    sol = Solution()