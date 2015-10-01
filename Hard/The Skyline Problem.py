# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
http://segmentfault.com/a/1190000003786782
http://www.cnblogs.com/easonliu/p/4531020.html
堆插入 堆调整
'''

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
                # heap.append(-h[1])
                heap.insert(self.getInsertPos(buildings, -h[1]), -h[1])
            else:
                heap.remove(h[1])
            cur = max(heap)
            if cur != pre:
                res.append([h[0], cur])
                pre = cur
        return res

    def getInsertPos(self, nums, ins):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] < ins:     # mid这个位置肯定不可取
                left = mid + 1
            elif nums[mid] > ins:
                right = mid - 1
            else:
                return mid
        return left

if __name__ == '__main__':
    sol = Solution()
    # print(sol.getInsertPos([1,2 ,3,7],7))
    print(sol.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))