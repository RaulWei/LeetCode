# -*- coding: UTF-8 -*-
__author__ = 'wang'

class Solution(object):
    # :type nums: List[int]
    # :rtype: List[int]
    def singleNumber(self, nums):
        res = [0, 0]
        # 先求出a和b的异或
        axorb = 0
        for n in nums:
            axorb ^= n
        # a和b相异 因此axorb中必有至少一位为1
        diff = axorb
        diff &= -diff
        for n in nums:
            if n & diff == 0:
                res[0] ^= n
            else:
                res[1] ^= n
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNumber([1, 2, 1, 3, 2, 5]))