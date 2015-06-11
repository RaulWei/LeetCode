# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
所谓的majority element一定超过半数
等于半数都不行
所有majority element只有一个
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        dict = {}
        for i in nums:
            if dict.has_key(i):
                dict[i] += 1
            else:
                dict[i] = 1
            if dict[i] > len(nums)/2:
                    return i

if __name__ == '__main__':
    sol = Solution()
    print(sol.majorityElement([1,2,3,3,3]))
