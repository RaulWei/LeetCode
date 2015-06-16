# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
1->2->3, 20000000000
超过最大递归深度了 对k剪枝 k %= lens
递归简单模拟 虽然最后过了 不过速度不是一般的慢
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
    def rotateRight(self, head, k):
        if not head:
            return None
        if k <= 0:
            return head
        virtual = ListNode(-1)
        pre, cur = virtual, head
        pre.next = head
        lens = 1
        while cur.next:
            cur = cur.next
            pre = pre.next
            lens += 1
        # lens表示链表长度 对k剪枝
        if lens <= k:
            k %= lens
            if k == 0:
                return head
        # 此时cur指向链表最后一个
        if cur != head:
            # cur==head说明链表只有一个节点 那么怎么旋转都是自己
            cur.next = head
            pre.next = None
        return self.rotateRight(cur, k-1)

if __name__ == '__main__':
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    sol = Solution()
    sol.rotateRight(p1, 2)
    pass
