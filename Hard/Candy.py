# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
两遍循环
第一遍：从左到右 随着排名增高 得到糖果也增多
第二遍：从右到左 随着排名增高 推算糖果数 如有需要则更新
最后返回糖果总数
'''

class Solution(object):
    # :type ratings: List[int]
    # :rtype: int
    def candy(self, ratings):
        getCandys = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                getCandys[i] = getCandys[i - 1] + 1
        for i in range(1, len(ratings))[::-1]:
            if ratings[i] < ratings[i - 1]:
                getCandys[i - 1] = max(getCandys[i - 1], getCandys[i] + 1)
        return sum(getCandys)

if __name__ == '__main__':
    sol = Solution()
    print(sol.candy([1, 2, 3]))
    print(sol.candy([1, 2, 2, 1]))
    print(sol.candy([3, 1, 2, 3, 2, 1]))
    print(sol.candy([3, 1, 3, 2, 1]))
