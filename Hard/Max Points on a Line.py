# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
http://fisherlei.blogspot.jp/2013/12/leetcode-max-points-on-line-solution.html
https://leetcode.com/discuss/9011/c-o-n-2-solution-for-your-reference
map中不要以斜率为key 因为斜率是小数 如果是无穷小数的时候会截断导致不准确 以(分子, 分母)为key比较好
特殊情况
1 垂直 斜率无穷大
2 重复节点
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
        max_points = 0
        for p1 in points:   # 固定某个点 找其他点与该点构成的直线的斜率 以哈希表记录相同斜率个数
            slope, copy, inner_max_points = dict(), 0, 0
            for p2 in points:
                if p1 == p2:
                    continue
                elif p1.x == p2.x and p1.y == p2.y:     # 重复节点 记录copy数
                    copy += 1
                else:
                    fz = p1.y - p2.y
                    fm = p1.x - p2.x
                    gcd = self.gcd(fz, fm)
                    fz /= gcd
                    fm /= gcd
                    if (fz, fm) in slope:   # list不能为dict的key 所以用元组
                        slope[(fz, fm)] += 1
                    else:
                        slope[(fz, fm)] = 1
                    inner_max_points = max(inner_max_points, slope[(fz, fm)])
            max_points = max(max_points, inner_max_points + copy + 1)
        return max_points

    def gcd(self, fz, fm):
        if fm == 0:
            return fz
        return self.gcd(fm, fz % fm)

if __name__ == '__main__':
    sol = Solution()
    p1 = Point(1, 1)
    p2 = Point(1, 2)
    p3 = Point(1, 3)
    print(sol.maxPoints([p1, p2, p3]))