# -*- coding: UTF-8 -*-
__author__ = 'wang'

class Solution(object):
    # :type ratings: List[int]
    # :rtype: int
    def candy(self, ratings):
        getCandys = [0] * len(ratings)
        getCandys[0] = 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                getCandys[i] = getCandys[i - 1] + 1
            else:
                getCandys[i] = 1
                j = i
                while ratings[j] < ratings[j - 1]:
                    if getCandys[j] >= getCandys[j - 1]:
                        getCandys[j - 1] += 1
                    j -= 1
        return sum(getCandys)

if __name__ == '__main__':
    sol = Solution()
    print(sol.candy([1, 2, 3]))
    print(sol.candy([1, 2, 2, 1]))
    print(sol.candy([3, 1, 2, 3, 2, 1]))
    print(sol.candy([3, 1, 3, 2, 1]))
