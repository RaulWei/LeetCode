# -*- coding: UTF-8 -*-
__author__ = 'weimw'

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

