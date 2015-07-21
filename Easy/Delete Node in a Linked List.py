# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
赋予当前node的值为下一个node的值
然后删除掉下一个node
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

