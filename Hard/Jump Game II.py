# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
f[i]表示从0到i需要的最少步数 初始化f[0]=0
根据每个nums[i]更新其后的nums[i]个f[i+x]的值
终态f[len(nums)-1]即为所求
注意剪枝
'''

# :type nums: List[int]
# :rtype: int
class Solution(object):
    def jump(self, nums):
        f = [32767] * len(nums)
        f[0] = 0
        # 循环每个nums[i] 求其后nums[i]个f的值
        for i in range(len(nums)):
            # 剪枝条件
            if i > 0 and nums[i] < nums[i - 1]:
                continue
            # 判断更新nums[i]后nums[i]个f值
            for j in range(1, nums[i] + 1):
                if i + j < len(nums) and f[i] + 1 < f[i + j]:
                    f[i + j] = f[i] + 1
        return f[len(nums) - 1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.jump([2, 3, 1, 1, 4]))
