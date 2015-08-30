# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution(object):
    # :type height: List[int]
    # :rtype: int
    def largestRectangleArea(self, height):
        max_area = 0
        for i in range(len(height)):
            # 找最左
            left = i
            while left > 0 and height[left - 1] >= height[i]:
                left -= 1
            # 找最右
            right = i
            while right < len(height) - 1 and height[right + 1] >= height[i]:
                right += 1
            # 算面积 更新max
            area = (right - left + 1) * height[i]
            if area > max_area:
                max_area = area
        return max_area

if __name__ == '__main__':
    sol = Solution()
    print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))
