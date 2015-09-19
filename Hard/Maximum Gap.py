# -*- coding: UTF-8 -*-
__author__ = 'wang'

import math

'''
给定无序数组 找出排序后的序列中两个相邻元素之间的最大差值
这种偏数学题的 需要注意很多边界的题目做起来还是很操蛋的
'''

class Solution(object):
    # :type nums: List[int]
    # :rtype: int
    def maximumGap(self, nums): # nums中的数都是非负的 并且在32bit范围内
        N = len(nums)
        if N < 2:
            return 0
        min_n, max_n = min(nums), max(nums)
        bk_len = int(math.ceil(float(max_n - min_n) / (N - 1)))   # ceil表示向上取整 bk_len表示每个区间长度
        bk_num = N # bk_num表示区间个数
        bks = [[] for i in range(bk_num)]    # 区间范围 左闭右开（最后一个区间双闭） [min, min+bk_len) [min+2*bk_len, min+3*bk_len) .. [min+n*bk_len, max]
        for n in nums:
            loc = (n - min_n) / bk_len
            bks[loc].append(n)
        max_gap = 0
        for i in range(1, len(bks)):
            max_gap = max(max_gap, min(bks[i]) - max(bks[i - 1]))
        return max_gap

if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumGap([3, 2, 3]))