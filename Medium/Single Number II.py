# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
按位(bit)计算
如果独数在该位有值 则sum(所有数在该位的值)%3==1
如果独数在该位无值 则sum(所有数在该位的值)%3==0
res记录最后结果 每次用|更新
注意：res有可能是负数 特殊处理
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        res = 0
        for i in range(32):
            bit_sum = 0
            for j in nums:
                bit_sum += ((j >> i) & 1)
            res |= (bit_sum % 3) << i
        if res >= 2**31:
            # 最高位为1 说明是负数
            return res - 2**32
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNumber([1, 2, 3, 9999999, 2, 1, 3, 3, 2, 1]))
