# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution(object):
    # :type n: int
    # :rtype: int
    def nthUglyNumber(self, n):
        idx1, idx2, idx3 = 0, 0, 0
        ugly_num = [1]
        for i in range(n):
            tmp = min(ugly_num[idx1] * 2, ugly_num[idx2] * 3, ugly_num[idx3] * 5)
            ugly_num.append(tmp)
            idx1 += 1 if tmp == ugly_num[idx1] * 2 else 0
            idx2 += 1 if tmp == ugly_num[idx2] * 3 else 0
            idx3 += 1 if tmp == ugly_num[idx3] * 5 else 0
        return ugly_num[n - 1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.nthUglyNumber(4))


