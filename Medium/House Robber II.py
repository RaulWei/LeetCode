# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
基于House Robber, 只需要把circle打破, 搞成row即可
分类讨论：
1 第n-1个没偷, 那么第0~n-2个跟House Robber一样;
2 第n-1个偷了, 那么第0和第n-2不能偷, 那么第1~n-3跟House Robber一样

House Robber
f(n)表示以n为结尾（取了n）的最大和
初始： f(low)=nums[low]
终态： max{f(n)}, low <= n <= high
递推公式： f(n) = max{f(i)} + nums[n], i < n-1(i不能取n-1 题目要求不能相邻)
'''

class Solution:
    def rowRob(self, nums, low, high):
        f = [0 for col in range(high+1)]
        f[low] = nums[low]
        for i in range(low+1, high + 1):
            maxf = 0
            for j in range(i-1):
                # 不能相邻 所以上限为i-1(取不到i-1 最多取i-2)
                if maxf < f[j]:
                    maxf = f[j]
            f[i] = maxf + nums[i]
        return max(f)

    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
        return max(self.rowRob(nums, 0, len(nums)-2), self.rowRob(nums, 1, len(nums)-3)+nums[-1])

if __name__ == '__main__':
    sol = Solution()
    print(sol.rob([4, 1, 2, 7, 5, 3, 1]))
