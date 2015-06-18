# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
从一组无序数中找最长的连续数的长度
利用"判断一个数是否在一个集合中"用时短的特性
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        # 把nums从list转换为set极其重要 判断if x in set比判断if x in list快的多
        nums = set(nums)
        longest = 0
        while nums:
            t = nums.pop()
            start, end = t, t
            while start - 1 in nums:
                # 往左边拓展
                start -= 1
                nums.remove(start)
            while end + 1 in nums:
                # 往右边拓展
                end += 1
                nums.remove(end)
            longest = max(longest, end - start + 1)
        return longest

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
