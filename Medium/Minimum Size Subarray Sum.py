# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
滑动窗口法
先移动e指针找到符合情况
再移动b指针缩小尝试范围
'''

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        lenth = len(nums)
        minLen = lenth + 1
        b, e, sum = 0, 0, 0
        while e < lenth:
            while sum < s and e < lenth:
                # e向右 拓展sum
                sum += nums[e]
                e += 1
            if sum < s:
                # 从b开始到最后 所有nums的和加起来都比s小
                break
            while b < e and sum >= s:
                # b向右 缩小sum
                sum -= nums[b]
                b += 1
            if minLen > e - b + 1:
                minLen = e - b + 1
        if minLen <= lenth:
            return minLen
        return 0

if __name__ == '__main__':
    sol = Solution()
    print(sol.minSubArrayLen(7, [2,3,1,2,4,9]))