# -*- coding: UTF-8 -*-
__author__ = 'Wang'

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        # 循环nums 如果i已经在字典中则说明有重复
        res = {}
        for i in nums:
            if res.has_key(i):
                return True
            res[i] = 1
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.containsDuplicate([1,1,2,3]))
    print(sol.containsDuplicate([1,2,3,4]))
