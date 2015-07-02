# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
两条竖线与x轴组成的区域 收集最多雨水
初始化最大面积为最左边和最右边以及x轴组成的区域
两条竖线往中间靠拢要使得面积变大 即长度缩短面积变大的条件是两竖线高度增加
时间复杂度为 O(N)
'''

class Solution:
    def getArea(self, height, left, right):
        if right >= left:
            return min(height[left], height[right]) * (right - left)
        return 0

    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        mArea = 0
        while left < right:
            mArea = max(mArea, self.getArea(height, left, right))
            if height[left] < height[right]:
                # 更新短竖线 因为固定短竖线 长竖线再怎么变长 也不能使得面积变大
                left += 1
                while height[left - 1] >= height[left] and left < len(height) - 1:
                    # 找到第一个比原短竖线长的 更新短竖线
                    left += 1
            else:
                right -= 1
                while height[right] <= height[right + 1] and right > 0:
                    right -= 1
        return mArea


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxArea([1, 1]))
    print(sol.maxArea([1, 2, 4, 3]))
    print(sol.maxArea([2, 3, 10, 5, 7, 8, 9]))