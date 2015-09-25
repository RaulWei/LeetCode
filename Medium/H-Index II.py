# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
二分法加速
'''

class Solution(object):
    # :type citations: List[int]
    # :rtype: int
    def hIndex(self, citations):
        if not citations or citations[-1] == 0:
            return 0
        length = len(citations)
        left, right = 0, length - 1
        while left < right:
            mid = (left + right) / 2
            if length - mid <= citations[mid]:
                right = mid
            else:
                left = mid + 1
        return length - right

if __name__ == '__main__':
    sol = Solution()
    print(sol.hIndex([11, 15]))
    print(sol.hIndex([0, 0, 1]))
    print(sol.hIndex([100]))
    print(sol.hIndex([1, 2, 3, 4, 5, 6]))
    print(sol.hIndex([0, 1, 3, 5, 6]))
