# -*- coding: UTF-8 -*-
__author__ = 'weimw'

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    # :type head: RandomListNode
    # :rtype: RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None
        # 复制next指针
        old = head
        while old:
            new = RandomListNode(old.label)
            new.next = old.next
            old.next = new
            old = new.next
        # 复制random指针
        old, new = head, head.next
        while old and new:
            if old.random:
                new.random = old.random.next
            old = new.next
            new = old.next if old else None
        # 拆分链表
        old, new, ret = head, head.next, head.next
        while old and new:
            old.next = new.next
            old = old.next
            new.next = old.next if old else None
            new = new.next
        return ret

if __name__ == '__main__':
    sol = Solution()
    p1 = RandomListNode(1)
    p2 = RandomListNode(2)
    p3 = RandomListNode(3)
    p4 = RandomListNode(4)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p1.random = p3
    p2.random = p4
    p = sol.copyRandomList(p1)
