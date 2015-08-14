# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        res, maxleft, maxright, left, right = 0, 0, 0, 0, len(height) - 1
        while left <= right:
            if height[left] < height[right]:
                if height[left] > maxleft:
                    maxleft = height[left]
                else:
                    res += maxleft - height[left]
                left += 1
            else:
                if height[right] > maxright:
                    maxright = height[right]
                else:
                    res += maxright - height[right]
                right -= 1
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))