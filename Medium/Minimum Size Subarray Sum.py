# -*- coding: UTF-8 -*-
__author__ = 'Wang'

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        lenth = len(nums)
        minLen = lenth
        b, e, sum = 0, 0, 0
        while e < lenth:
            while sum < s and e < lenth:
                # e向右 拓展sum
                sum += nums[e]
                e += 1
            if sum < s:
                # 所有nums的和加起来都比s小
                return 0
            while b < e and sum >= s:
                # b向右 缩小sum
                sum -= nums[b]
                b += 1
            if minLen > e - b + 1:
                minLen = e - b + 1
        return minLen

if __name__ == '__main__':
    sol = Solution()
    print(sol.minSubArrayLen(7, [2,3,1,2,4,9]))