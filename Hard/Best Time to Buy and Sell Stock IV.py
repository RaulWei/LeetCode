# -*- coding: UTF-8 -*-
__author__ = 'wang'

class Solution(object):
    # :type k: int
    # :type prices: List[int]
    # :rtype: int
    def maxProfit(self, K, prices):
        if not prices:
            return 0

        max_prof = 0
        f = [[0 for col in range(len(prices))] for row in range(K + 1)]

        # 递推
        for k in range(1, K + 1):
            max_tmp = f[k - 1][0] - prices[0]
            for i in range(1, len(prices)):
                f[k][i] = max(f[k][i - 1], prices[i] + max_tmp)
                max_tmp = max(max_tmp, f[k - 1][i] - prices[i])
                max_prof = max(max_prof, f[k][i])

        return max_prof

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit(0, []))
    print(sol.maxProfit(2, [1, 1, 2, 1, 1]))
    print(sol.maxProfit(2, [1, 2, 3, 1, 2, 4]))