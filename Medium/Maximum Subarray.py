# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
简单dp
设f(n)以nums[n]结尾的包含nums[n]的最大连续子数组
初态： f(0) = nums[0]
终态： max(f[n]) 0 <= n < len(nums)
递推公式： f(n) = max{f(n-1), 0} + nums[n], 因为题目要求连续子数组 所以包含nums[n]的话
要么包含nums[n-1] 要么单独nums[n]
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        f = [nums[0]]
        for i in range(1, len(nums)):
            f.append(max(f[i - 1], 0) + nums[i])
        return max(f)

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
