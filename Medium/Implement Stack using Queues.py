# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
手动实现栈
可以利用python标准库
我直接用list模拟
水题中的战斗机
'''

class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.base = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.base.append(x)

    # @return nothing
    def pop(self):
        self.base.pop()

    # @return an integer
    def top(self):
        return self.base[len(self.base) - 1]

    # @return an boolean
    def empty(self):
        if not self.base:
            return True
        return False
