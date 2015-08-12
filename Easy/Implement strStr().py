# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if not needle:
            # needle是0 说明是可以从haystack找到needle的
            return 0
        if not haystack or len(haystack) < len(needle):
            return -1
        p1, p2 = 0, len(needle)
        while p2 <= len(haystack):
            # 固定窗口大小进行滑动
            if haystack[p1:p2] == needle:
                return p1
            p1 += 1
            p2 += 1
        return -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.strStr('a', ''))

