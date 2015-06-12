# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        rv = digits[::-1]
        for i in range(len(rv)):
            if rv[i] + 1 <= 9:
                rv[i] += 1
                break
            elif rv[i] + 1 > 9 and i != len(rv) - 1:
                rv[i] = 0
            else:
                rv[i] = 0
                rv.append(1)
        return rv[::-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.plusOne([9,9,9]))
    print(sol.plusOne([9,9,8]))
    print(sol.plusOne([9,8,9]))
