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
        diff &= -diff   # 找出diff中为1的那一位（设为第*位） 置其他位全为0 用来对原nums分类
        for n in nums:
            # 第*位为0的分为一类 第*位为1的分为一类 nums中两个不同的数必然分别处于这两类中
            # 再用之前single number题目中求异或的方法分别把这两个数找出来
            if n & diff == 0:
                res[0] ^= n
            else:
                res[1] ^= n
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNumber([1, 2, 1, 3, 2, 5]))