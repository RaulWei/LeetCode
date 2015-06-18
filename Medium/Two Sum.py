# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
在一个数组中找到两个数 使得这两个数的和为target
按从小到大顺序返回这两个数的下标
利用字典完成O(n)算法
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dict = {}
        res = []
        for i in range(len(nums)):
            if target - nums[i] in dict:
                # 如果target - nums[i]在字典中了 说明两个数都找到了 返回结果
                res.append(dict[target - nums[i]] + 1)
                res.append(i + 1)
                return res
            # 否则把当前数以及下标插入字典
            dict[nums[i]] = i

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))
