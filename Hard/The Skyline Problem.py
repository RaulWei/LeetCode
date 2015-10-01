# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution(object):
    # :type buildings: List[List[int]]
    # :rtype: List[List[int]]
    def getSkyline(self, buildings):
        height = []
        for b in buildings:
            height.append([b[0], -b[2]])
            height.append([b[1], b[2]])
        height = sorted(height)
        heap, res = [0], []
        pre, cur = 0, 0
        for h in height:
            if h[1] < 0:
                heap.append(-h[1])
            else:
                heap.remove(h[1])
            cur = max(heap)
            if cur != pre:
                res.append([h[0], cur])
                pre = cur
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))