# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
两条竖线与x轴组成的区域 收集最多雨水
'''

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        left, right = height[0], height[-1]
        area = min(left, right) * (right - left)
        while left < right:
        pass

if __name__ == '__main__':
    sol = Solution()