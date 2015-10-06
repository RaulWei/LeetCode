# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
掌握规律就不难 没掌握规律就很难
k[0] = 1
k[1] = min(k[0] * 2, k[0] * 3, k[0] * 5) = min(2, 3, 5) = 2
k[2] = min(k[1] * 2, k[0] * 3, k[0] * 5) = min(4, 3, 5) = 3
k[3] = min(k[1] * 2, k[1] * 3, k[0] * 5) = min(4, 6, 5) = 4
k[4] = min(k[2] * 2, k[1] * 3, k[0] * 5) = min(6, 6, 5) = 5
k[5] = min(k[2] * 2, k[1] * 3, k[1] * 5) = min(6, 6, 10) = 6
k[6] = min(k[3] * 2, k[2] * 3, k[1] * 5) = min(8, 9, 10) = 8
...
'''

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
