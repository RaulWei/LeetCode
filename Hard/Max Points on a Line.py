# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
http://fisherlei.blogspot.lt/2013/12/leetcode-max-points-on-line-solution.html
https://leetcode.com/discuss/9011/c-o-n-2-solution-for-your-reference
map中不要以斜率为key 因为斜率是小数 如果是无穷小数的时候会截断导致不准确 以[分子, 分母]为key比较好
'''

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    # :type points: List[Point]
    # :rtype: int
    def maxPoints(self, points):
        pass

if __name__ == '__main__':
    sol = Solution()