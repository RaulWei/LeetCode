# -*- coding: UTF-8 -*-
__author__ = 'Wang'

class Solution:
    def myQSort(self, nums, k, left, right):
        pivot = nums[left]
        i, j = left, right
        while i < j:
            while nums[j] >= pivot and i < j:
                j -= 1
            while nums[i] <= pivot and i < j:
                i += 1
            if i < j:
                t = nums[j]
                nums[j] = nums[i]
                nums[i] = t
        nums[left] = nums[i]
        nums[i] = pivot
        len_nums = right - left + 1
        if k == len_nums - (i - left):
            return nums[i]
        elif k < len_nums - (i - left):
            # pivot的右边 即都大于pivot
            return self.myQSort(nums, k, i + 1, right)
        else:
            # pivot的左边 即都小于pivot
            return self.myQSort(nums, k - len_nums + i - left, left, i - 1)

    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        return self.myQSort(nums, k, 0, len(nums) - 1)

if __name__ == '__main__':
    sol = Solution()
    print(sol.findKthLargest([3,2,1,5,6,4], 2))
    print(sol.findKthLargest([1], 1))
    print(sol.findKthLargest([2, 2], 1))