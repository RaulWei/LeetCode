# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
二分法 时间复杂度为O(log(min(len1, len2)))
边界情况要考虑清楚
'''

class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            # 确保nums1比nums2短
            nums1, nums2, len1, len2 = nums2, nums1, len2, len1

        imin, imax = 0, len1
        while imin <= imax:
            # 这样设置i,j会使得len1+len2为奇数时左边划分比右边多一个 偶数时两边一样多
            i = (imin + imax) / 2
            j = (len1 + len2 + 1) / 2 - i

            # 二分
            if i > 0 and j < len2 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            elif j > 0 and i < len1 and nums2[j - 1] > nums1[i]:
                imin = i + 1
            else:
                # 左右划分个数相同或左边多一个 并且左边划分都小于等于右边划分

                # 求左划分的最大
                if i == 0:
                    m1 = nums2[j - 1]
                elif j == 0:
                    m1 = nums1[i - 1]
                else:
                    m1 = max(nums1[i - 1], nums2[j - 1])

                if (len1 + len2) % 2 == 1:
                    # 两个数组一共有奇数个元素
                    return m1

                # 求右划分的最小
                if i == len1:
                    m2 = nums2[j]
                elif j == len2:
                    m2 = nums1[i]
                else:
                    m2 = min(nums1[i], nums2[j])

                return (m1 + m2) / 2.0


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMedianSortedArrays([], [1]))
    print(sol.findMedianSortedArrays([1, 2, 3, 4],[1, 2, 3, 4]))