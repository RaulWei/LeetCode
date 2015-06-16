# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
二分法求Sqrt(x)
掌握二分法的框架写法
重点把握边界条件
'''

class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        low = 0
        high = x
        while low < high:
            mid = (low + high) / 2
            if mid**2 < x:
                if low == mid:
                    break
                low = mid
            elif mid**2 > x:
                high = mid - 1
            else:
                return mid
        if high**2 <= x:
            return high
        return low

if __name__ == '__main__':
    sol = Solution()
    print(sol.mySqrt(144))
