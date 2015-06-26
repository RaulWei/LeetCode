# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
双指针思想
比如 given [0,1,2,4,5,7], return ["0->2","4->5","7"].
'''

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        res = []
        i = 0
        while i < len(nums):
            start, end = i, i
            while end < len(nums) - 1 and nums[end + 1] == nums[end] + 1:
                end += 1
            if start != end:
                res.append(str(nums[start]) + '->' + str(nums[end]))
            else:
                res.append(str(nums[start]))
            i = end + 1
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.summaryRanges([]))

