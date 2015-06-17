# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
这题A的艰难 乍一看挺简单的题 不断修改最后思路都乱了
'''

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        point = []
        for p in intervals:
            point.append([p.start, 's'])
            point.append([p.end, 'e'])
        # point.append([newInterval.start, 's'])
        # point.append([newInterval.end, 'e'])
        point.sort(lambda x, y: x[0] - y[0])
        b, e = 0, 0
        stack = []
        res = []
        for p in point:
            if p[1] == 's':
                if not stack:
                    b = p[0]
                stack.append(p[1])
            else:
                stack.pop()
                if not stack:
                    e = p[0]
                    t = intervals.pop()
                    t.start = b
                    t.end = e
                    res.append(t)
        i = 0
        while i < len(res) - 1:
            if res[i].end == res[i + 1].start:
                res[i].end = res[i + 1].end
                res.remove(res[i + 1])
                i = 0
                continue
            i += 1
        return res

if __name__ == '__main__':
    p1 = Interval(1, 5)
    p2 = Interval(1, 3)
    p3 = Interval(5, 11)
    p4 = Interval(0, 3)
    p5 = Interval(6, 8)
    inter = [p1]
    sol = Solution()
    print(sol.insert(inter, p5))

