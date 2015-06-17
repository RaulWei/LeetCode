# -*- coding: UTF-8 -*-
__author__ = 'Wang'

'''
求max(price[i] - price[j]), i>j
low记录当前走过的最低价
res记录当前走过的最高收益
'''

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if not prices:
            return 0
        low = prices[0]
        res = 0
        for i in prices:
            if low > i:
                low = i
            if res < i - low:
                res = i - low
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([3, 10, 1, 10, 2]))
