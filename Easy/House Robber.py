# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
动态规划 一组数 不能取相邻的数 要使所取的数和最大
f(n)表示以n为结尾（取了n）的最大和
初始： f(0)=0 f(1)=nums[0]
终态： max{f(n)}, 1 <= n <= len(nums)
递推公式： f(n) = max{f(i)} + nums[n], i < n-1(i不能取n-1 题目要求不能相邻)
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
            return 0
        f = [0, nums[0]]
        for i in range(2, len(nums) + 1):
            maxf = 0
            for j in range(i-1):
                # 不能相邻 所以上限为i-1(取不到i-1 最多取i-2)
                if maxf < f[j]:
                    maxf = f[j]
            f.append(maxf + nums[i - 1])
        return max(f)

if __name__ == '__main__':
    sol = Solution()
    print(sol.rob([2, 2, 2, 2, 2, 2, 2, 1, 1, 2]))
