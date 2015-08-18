# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
3个for 时间复杂度必然不会低
根据3Sum修改的 固定前两个数得到newTarget
这样就把题目转换为TwoSum
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        s = set()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                newTarget = target - nums[i] - nums[j]
                dict, res = {}, []
                for k in range(j + 1, len(nums)):
                    if newTarget - nums[k] in dict:
                        res.append(nums[i])
                        res.append(nums[j])
                        res.append(nums[k])
                        res.append(newTarget - nums[k])
                        res.sort()
                        s.add(tuple(res))
                        res = []
                    dict[nums[k]] = k
        ret = []
        for t in s:
            ret.append(list(t))
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))