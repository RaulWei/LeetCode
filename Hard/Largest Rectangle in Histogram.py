# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution(object):
    # :type height: List[int]
    # :rtype: int
    def largestRectangleArea(self, height):
        height.append(0)
        left_area, right_area, max_area = 0, 0, 0
        i, stack = 0, []
        while i < len(height):
            while stack and height[i] < height[stack[-1]]:
                tmp = stack.pop()
                left_area = height[tmp] * (tmp + 1 if not stack else tmp - stack[-1])
                right_area = height[tmp] * (i - tmp - 1)
                area = left_area + right_area
                max_area = area if area > max_area else max_area
            stack.append(i)
            i += 1
        return max_area

if __name__ == '__main__':
    sol = Solution()
    print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))
