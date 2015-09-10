# -*- coding: UTF-8 -*-

'''
只能是买-卖-买-卖这样 不能有买-买-卖-卖这样的情况
'''

class Solution(object):
    # :type prices: List[int]
    # :rtype: int
    def maxProfit(self, prices):
        res = 0
        for i in range(0, len(prices) - 1):
            if prices[i + 1] > prices[i]:
                res += prices[i + 1] - prices[i]
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([1, 1, 2, 3, 4, 5, 5, 0]))