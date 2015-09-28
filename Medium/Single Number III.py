# -*- coding: UTF-8 -*-
__author__ = 'wang'

class Solution(object):
    # :type nums: List[int]
    # :rtype: List[int]
    def singleNumber(self, nums):
        # 先拿到a和b的异或
        axorb = 0
        for i in range(nums):
            axorb ^= i
        pass

if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNumber([1, 2, 1, 3, 2, 5]))