# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
http://segmentfault.com/a/1190000003786782
http://www.cnblogs.com/easonliu/p/4531020.html
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
                heap.insert(self.getInsertPos(heap, -h[1]), -h[1])
            else:
                heap.remove(h[1])
            cur = heap[-1]
            if cur != pre:
                res.append([h[0], cur])
                pre = cur
        return res

    # :type nums: List[int] 一个升序数组
    # :type ins: int 一个待插入的值
    # :rtype: int 插入的位置
    def getInsertPos(self, nums, ins):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] < ins:     # mid这个位置肯定不可取 保证left可行性 所以最后return left
                left = mid + 1
            elif nums[mid] > ins:
                right = mid - 1     # mid说不定可取 但令right=mid-1 不保证right一定正确
            else:
                return mid
        return left

if __name__ == '__main__':
    sol = Solution()
    print(sol.getInsertPos([0],7))
    print(sol.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))