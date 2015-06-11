# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
栈元素 (x,curMin)
保存每个元素插入时的当前最小值
'''

class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        curMin = self.getMin()
        if curMin is None or x < curMin:
            curMin = x
        self.stack.append((x, curMin))
        return x

    # @return nothing
    def pop(self):
        # 之前用self.stack.remove()就一直超时
        # remove O(n); pop O(n-i); del O(n-i)
        self.stack.pop()
        return

    # @return an integer
    def top(self):
        if not self.stack:
            return None
        return self.stack[len(self.stack)-1][0]

    # @return an integer
    def getMin(self):
        if not self.stack:
            return None
        return self.stack[len(self.stack)-1][1]

if __name__ == '__main__':
    stack = MinStack()
    stack.push(-3)
    stack.push(-2)
    stack.push(-1)
    print(stack.getMin())
    stack.pop()
    print(stack.getMin())
    print(stack.top())
