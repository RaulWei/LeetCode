# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums.sort()
        s = set()
        dict = {}
        for i in range(len(nums) - 2):
            target = -1 * nums[i]
            for j in range(i + 1, len(nums) - 1):
                res = []
                if target - nums[j] in dict:
                    res.append(nums[i])
                    res.append(nums[j])
                    res.append(target - nums[j])
                    res.sort()
                    s.add(tuple(res))
                dict[nums[j]] = j
        ret = []
        for t in s:
            ret.append(list(t))
        return ret

if __name__ == '__main__':
    sol = Solution()
    # print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
    print(sol.threeSum([1, 2, -2, -1]))