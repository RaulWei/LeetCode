# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
f[k, i]表示从prices[0]到prices[i]经过k次transactions所能够获得的最大收益
初态：f[0, i] = 0 （0次transaction当然收益为0） f[k, 0] = 0 （prices只有一个 实现不了买入卖出操作 至少要两个节点）
终态：max(f[k, i])
递推公式：
f[k, i] = max(f[k, i - 1], prices[i] - prices[j] + f[k - 1, j]) 0 < j < i
'''

class Solution(object):
    # :type prices: List[int]
    # :rtype: int
    def maxProfit(self, prices):
        K, max_prof = 2, 0
        f = [[0 for col in range(len(prices))] for row in range(K + 1)]

        # 递推
        for k in range(1, K + 1):
            for i in range(1, len(prices)):
                max_tmp = 0
                for j in range(i):
                    tmp = prices[i] - prices[j] + f[k - 1][j]
                    if tmp > max_tmp:
                        max_tmp = tmp
                f[k][i] = max(f[k][i - 1], max_tmp)
                max_prof = max(max_prof, f[k][i])

        return max_prof

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([1, 1, 2, 1, 1]))
    print(sol.maxProfit([1, 2, 3, 1, 2, 4]))