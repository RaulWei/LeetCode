# -*- coding: UTF-8 -*-
__author__ = 'weimw'


class Solution(object):
    # :type n: int
    # :type k: int
    # :rtype: str
    def getPermutation(self, n, k):
        nums = [str(n) for n in range(1, n + 1)]
        p, res = 1, []
        for n in range(1, n + 1):
            p *= n
        k -= 1

        for i in range(n):
            p /= n - i
            select = k / p
            res.append(nums[select])

            for j in range(select, n - i - 1):
                nums[j] = nums[j + 1]
            k %= p
        return ''.join(res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.getPermutation(1, 1))
