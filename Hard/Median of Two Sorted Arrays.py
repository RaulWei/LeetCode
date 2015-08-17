# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        len1, len2 = len(nums1), len(nums2)
        end = (len1 + len2) / 2
        if len1 >= end:
            for i in range(end + 1):
                j = end - i
                if j < len2 and (j + 1 == len2 or nums1[i] <= nums2[j + 1]) and (i + 1 == len1 or nums2[j] <= nums1[i + 1]):
                    break
            return min(nums1[i + 1], nums2[j + 1])
        else:
            for j in range(end + 1):
                i = end - j
                if i < len1 and (j + 1 == len2 or nums1[i] <= nums2[j + 1]) and (i + 1 == len1 or nums2[j] <= nums1[i + 1]):
                    break
            return min(nums1[i + 1], nums2[j + 1])

if __name__ == '__main__':
    sol = Solution()
    print(sol.findMedianSortedArrays([1,2,3,4],[1,2,3,4]))