# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
双指针 i 和 j
利用原数组已排序的特征
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i = 0
        j = 0
        len_nums = len(nums)
        while i < len_nums:
            if nums[i] == nums[j]:
                i += 1
            else:
                j += 1
                nums[j] = nums[i]
                i += 1
        return j + 1

if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates([1, 1, 1, 2, 3, 3]))
    print(sol.removeDuplicates([]))
    print(sol.removeDuplicates([1, 1, 1, 1, 1]))