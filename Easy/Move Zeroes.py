# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution(object):
    # :type nums: List[int]
    # :rtype: void Do not return anything, modify nums in-place instead.
    def moveZeroes(self, nums):
        seat, i = 0, 0  # seat用来记录已经归位的0的个数
        while i < len(nums) - seat:
            if nums[i] == 0:
                for j in range(i, len(nums) - seat - 1):
                    # 类似冒泡的向后交换
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                seat += 1
                i = 0   # 串尾有0归位了 但是串前部可能打乱了 所以i要置0重新开始
            else:
                i += 1
        return nums

if __name__ == '__main__':
    sol = Solution()
    print(sol.moveZeroes([0, 0, 1]))
    print(sol.moveZeroes([0, 1, 0, 3, 12]))