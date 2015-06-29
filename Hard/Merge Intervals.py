# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
贴了Insert Interval.py代码
一模一样的思路 1A
'''

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        point = []
        for p in intervals:
            # 把所有点在数轴上排序
            point.append([p.start, 's'])
            point.append([p.end, 'e'])
        point.sort(lambda x, y: x[0] - y[0])

        b, e = 0, 0
        stack = []
        res = []
        for p in point:
            # 利用栈合并区间
            if p[1] == 's':
                if not stack:
                    b = p[0]
                stack.append(p[1])
            else:
                stack.pop()
                if not stack:
                    e = p[0]
                    # 题目要求in-place 不可以自己再申请Interval 要利用原来的
                    t = intervals.pop()
                    t.start = b
                    t.end = e
                    res.append(t)

        # 到这步有了初步的res 接下来要把特殊情况如[1,5][5,7]这样的合并
        i = 0
        while i < len(res) - 1:
            if res[i].end == res[i + 1].start:
                res[i].end = res[i + 1].end
                res.remove(res[i + 1])
                i = 0
                continue
            i += 1
        return res
