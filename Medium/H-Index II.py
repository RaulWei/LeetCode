# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
二分法加速
'''

class Solution(object):
    # :type citations: List[int]
    # :rtype: int
    def hIndex(self, citations):
        length = len(citations)
        # left, right = 0, length - 1
        # while left < right:
        #     mid = (left + right) / 2
        for i in range(length):
            if length - i < citations[i]:
                return i + 1
            j = length - 1 - i
            if length - j >= citations[j]:
                return citations[j]
        return 0

if __name__ == '__main__':
    sol = Solution()
    print(sol.hIndex([100]))
    print(sol.hIndex([0, 1, 3, 5, 6]))
