# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
给定的n代表有[1, 2, .. n]这么多个版本号 其中某个版本坏了 导致其之后的版本全都坏了
所以要快速找到第一个坏了的版本号
显然 二分法
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    # :type n: int
    # :rtype: int
    def firstBadVersion(self, n):
        left, right = 1, n
        while left < right:
            mid = (left + right) / 2
            if isBadVersion(mid):   # 第mid个版本是坏的 之后都是坏的
                right = mid
            else:
                left = mid + 1
        return right

