# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
f[k, i]表示从prices[0]到prices[i]最多经过k次transactions所能够获得的最大收益
初态：f[0, i] = 0 （0次transaction当然收益为0） f[k, 0] = 0 （prices只有一个 实现不了买入卖出操作 至少要两个节点）
终态：max(f[k, i])
递推公式：
f[k, i] = max(在i之前就已经得到最大利润, i处卖出 j处买入所获得的利润 + f[k - 1, j - 1])
        = max(f[k, i - 1], prices[i] - prices[j] + f[k - 1, j - 1]) 0 <= j < i
        = max(f[k, i - 1], prices[i] + max(f[k - 1, j - 1] - prices[j]) (0 <= j < i) ))
j的取值是[0,i) 没必要再来个循环求max(f[k - 1, j] - prices[j]) 这样会TLE 直接合在i的这层循环中做 两重循环不超时
'''

class Solution(object):
    # :type prices: List[int]
    # :rtype: int
    def maxProfit(self, K, prices):
        if not prices:
            return 0

        # 剪枝
        # 在i处只能买或者卖 当可交易次数超过len/2时 超过最频繁交易次数 肯定K有多余
        # 这种情况下求最大利润 只要相邻price有上升就可以计入总利润中
        if K > len(prices) / 2:
            ret = 0
            for i in range(1, len(prices)):
                ret += prices[i] - prices[i - 1] if prices[i] > prices[i - 1] else 0
            return ret

        # 动态规划
        f = [[0 for col in range(len(prices))] for row in range(2)] # 不需要申请K行 因为每次只用到 k 和 k-1 后面的操作用模就可以了
        for k in xrange(1, K + 1):  # 这里K很大 如果用range生成的list太大会报内存错误 所以这里用迭代器
            max_tmp = f[(k - 1) % 2][0] - prices[0]
            for i in range(1, len(prices)):
                f[k % 2][i] = max(f[k % 2][i - 1], prices[i] + max_tmp)
                max_tmp = max(max_tmp, f[(k - 1) % 2][i - 1] - prices[i])
        return f[K % 2][len(prices) - 1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit(0, []))
    print(sol.maxProfit(2, [1, 2, 3]))
    print(sol.maxProfit(2, [1, 1, 2, 1, 1]))
    print(sol.maxProfit(2, [1, 2, 3, 1, 2, 4]))