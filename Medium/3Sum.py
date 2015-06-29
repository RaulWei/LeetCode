# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
基于two sum 做了微小的改动
从左向右遍历 固定遍历到的数nums[i] 则target = 0 - nums[i]
确定了target 那么从i + 1开始直到len(nums) 就完全转换为two sum这题
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        # 利用集合的去重功能
        s = set()
        for i in range(len(nums) - 2):
            # 固定一个数 求出target
            target = -1 * nums[i]
            # 以下模仿two sum这个题 利用字典
            dict = {}
            res = []
            for j in range(i + 1, len(nums)):
                if target - nums[j] in dict:
                    res.append(nums[i])
                    res.append(nums[j])
                    res.append(target - nums[j])
                    res.sort()
                    s.add(tuple(res))
                    # 这里找到一组合法解 重置res 不能就此跳出循环 因为这里固定nums[i] 但是可能有多组不同的合法解
                    res = []
                dict[nums[j]] = j
        # set to list 并返回
        ret = []
        for t in s:
            ret.append(list(t))
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
    print(sol.threeSum([1, 2, -2, -1]))
    print(sol.threeSum([0, 0, 0]))