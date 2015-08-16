# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
m[i]表示以下标i结尾的连续最大乘积
n[i]表示以下标i结尾的连续最小乘积
初态：m[0] = n[0] = nums[0]
终态：max(m[0])
递归公式：
nums[i] >= 0: m[i] = max(m[i-1]*nums[i], nums[i]), n[i] = min(n[i-1]*nums[i], nums[i])
nums[i] < 0: m[i] = max(n[i-1]*nums[i], nums[i]), n[i] = min(m[i-1]*nums[i], nums[i])
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        m, n = [0] * len(nums), [0] * len(nums)
        m[0], n[0] = nums[0], nums[0]
        for i in range(len(nums))[1:]:
            m[i] = max(m[i - 1] * nums[i], nums[i]) if nums[i] >= 0 else max(n[i - 1] * nums[i], nums[i])
            n[i] = min(n[i - 1] * nums[i], nums[i]) if nums[i] >= 0 else min(m[i - 1] * nums[i], nums[i])
        return max(m)

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProduct([2, 3, -2, 4]))