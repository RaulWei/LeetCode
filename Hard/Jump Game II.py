# -*- coding: UTF-8 -*-
__author__ = 'weimw'

# :type nums: List[int]
# :rtype: int
class Solution(object):
    def jump(self, nums):
        f = [32767] * len(nums)
        f[0] = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] < nums[i - 1]:
                continue
            for j in range(1, nums[i] + 1):
                if i + j < len(nums) and f[i] + 1 < f[i + j]:
                    f[i + j] = f[i] + 1
        return f[len(nums) - 1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.jump([2, 3, 1, 1, 4]))
