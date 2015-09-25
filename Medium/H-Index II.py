# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
给定是一段排好序的数组 所以有了二分的前提
采用二分法加速
找到index 如果citations[index] >= length - index 那么这个index就是其中一种合法的index return的是length - index
但我们要找的是 max(length - index) 所以还要往左找
'''

class Solution(object):
    # :type citations: List[int]
    # :rtype: int
    def hIndex(self, citations):
        if not citations or citations[-1] == 0:
            # 特例处理
            return 0
        length = len(citations)
        left, right = 0, length - 1
        while left < right:
            mid = (left + right) / 2
            if length - mid <= citations[mid]:
                right = mid # 这个mid是合法的index 用right记录合法的index
            else:
                left = mid + 1  # 这个mid不合法 没必要为它浪费时间 所以令left为mid的下一个
        return length - right

if __name__ == '__main__':
    sol = Solution()
    print(sol.hIndex([11, 15]))
    print(sol.hIndex([0, 0, 1]))
    print(sol.hIndex([100]))
    print(sol.hIndex([1, 2, 3, 4, 5, 6]))
    print(sol.hIndex([0, 1, 3, 5, 6]))
