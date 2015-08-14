# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
乱序数组中找第一个未出现的整数
时间复杂度O(n) 空间复杂度O(1)

归位之后希望是A[0] = 1, A[1] = 2, A[i] = i+1, ..
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                # 将nums[i]归位 len(nums)应该归位到nums[len(nums)-1] 所以这里取了等号
                # 后一个判断 如果为 nums[i] != i+1 判断i处是否有归位数 这种判断处理[1, 1]用例死循环
                # 后一个判断 改为nums[nums[i]-1] != nums[i] 判断nums[i]这个数是否归位 可以处理重复数不陷入死循环
                t = nums[i]
                nums[i] = nums[t-1]
                nums[t-1] = t
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1

if __name__ == '__main__':
    sol = Solution()
    print(sol.firstMissingPositive([3, 4, -1, 1]))
    print(sol.firstMissingPositive([1, 1]))