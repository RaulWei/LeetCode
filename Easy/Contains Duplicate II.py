# -*- coding: UTF-8 -*-
__author__ = 'Wang'

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        dict = {}
        for i in range(len(nums)):
            if dict.has_key(nums[i]):
                if i - dict[nums[i]] <= k:
                    return True
            dict[nums[i]] = i
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.containsNearbyDuplicate([1,2],1))
