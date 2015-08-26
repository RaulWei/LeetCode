# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
给定一串数字 0,1,2,...,n 要求找其中miss了谁
通常解 missing num = 理想和 - 现实和
'''

class Solution(object):
    # :type nums: List[int]
    # :rtype: int
    def missingNumber(self, nums):
        fact_sum, max = 0, 0
        # 求现实和
        for n in nums:
            fact_sum += n
            if n > max:
                max = n
        # 求理想和 等差数列求和公式
        ideal_sum = (max * (max + 1)) / 2
        if ideal_sum == fact_sum:
            # 缺0
            if max == len(nums):
                return 0
            # 什么都不缺
            return max + 1
        return ideal_sum - fact_sum

if __name__ == '__main__':
    sol = Solution()
    print(sol.missingNumber([0]))
    print(sol.missingNumber([1]))
    print(sol.missingNumber([0, 1, 3]))
