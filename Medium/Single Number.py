# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
O(n)算法
按位异或可交换
(2^1^4^5^2^4^1) => ((2^2)^(1^1)^(4^4)^(5)) => (0^0^0^5) => 5

o(?)算法
r = 0
for i in nums
    if i in list
        r -= i
    else
        list.append(i)
        r += i
看似O(n) 实际上判断是否在list中很慢
此方法超时
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        r = 0
        for i in nums:
            r ^= i
        return r

if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNumber([1,2,1,3,3,4,2]))