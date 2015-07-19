# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
用栈实现队列
python下我用序列模拟栈来实现
'''

class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.q = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q.append(x)

    # @return nothing
    def pop(self):
        self.q = self.q[1::]

    # @return an integer
    def peek(self):
        if not q:
            return None
        return self.q[0]

    # @return an boolean
    def empty(self):
        if not self.q:
            return True
        return False

if __name__ == '__main__':
    q = Queue()
    q.push(1)
    q.push(2)
    q.pop()
    q.pop()

