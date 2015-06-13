# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
双指针归并排序
不能引入第三个数组
技巧：
1 确定排序后数组大小
2 从尾巴开始往前排序 这样免去移动nums1原数据的麻烦
'''

class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        index1 = m - 1
        index2 = n - 1
        index = m + n - 1
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] > nums2[index2]:
                nums1[index] = nums1[index1]
                index -= 1
                index1 -= 1
            else:
                nums1[index] = nums2[index2]
                index -= 1
                index2 -= 1
        while index2 >= 0:
            # nums1结束 nums2还有数没有归并
            nums1[index] = nums2[index2]
            index -= 1
            index2 -= 1
        print(nums1)
        return

if __name__ == '__main__':
    sol = Solution()
    sol.merge([1, 2, 3, 0, 0], 3, [1, 2], 2)
    sol.merge([ 0, 0], 0, [1, 2], 2)
    sol.merge([0], 0, [0], 0)
