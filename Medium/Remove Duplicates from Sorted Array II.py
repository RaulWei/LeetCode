# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
数组去重 每种数最多留N个 数组已经排序
[1,1,1,1,2,3,3] N=2 -> [1,1,2,3,3]

三指针
i 遍历原数组
j 指向结果数组
b 指向每种数的第一个
'''

N = 2
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        i, j, b = 0, 0, 0
        len_nums = len(nums)
        while i < len_nums:
            if nums[i] == nums[b]:
                if i - b < N:
                    nums[j] = nums[i]
                    i += 1
                    j += 1
                else:
                    i += 1
            else:
                b = i
        #print(nums)
        return j

if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates([1, 1, 1, 1, 2, 2, 3, 4]))
    print(sol.removeDuplicates([]))
    print(sol.removeDuplicates([1]))
    print(sol.removeDuplicates([0, 0, 0]))
