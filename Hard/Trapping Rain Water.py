# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
water[i]表示下标为i处能够收集的雨水
water[i] = min(maxleft, maxright) - height[i]

两边向中间扫 一次遍历解决
从左向右遍历到i 说明右边肯定有height比maxleft高 所以water[i] = maxleft - height[i]
从右向左遍历到i 说明左边肯定有height比maxright高 所以water[i] = maxright - height[i]
'''

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