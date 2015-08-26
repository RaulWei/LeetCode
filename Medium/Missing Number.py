# -*- coding: UTF-8 -*-
__author__ = 'wang'

class Solution(object):
    # :type nums: List[int]
    # :rtype: int
    def missingNumber(self, nums):
        fact_sum, max = 0, 0
        for n in nums:
            fact_sum += n
            if n > max:
                max = n
        ideal_sum = (max * (max + 1)) / 2
        if ideal_sum == fact_sum:
            return max + 1
        return ideal_sum - fact_sum

if __name__ == '__main__':
    sol = Solution()
    print(sol.missingNumber([0]))
    print(sol.missingNumber([1]))
    print(sol.missingNumber([0, 1, 3]))
