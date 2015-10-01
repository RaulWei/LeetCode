# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
http://segmentfault.com/a/1190000003786782
http://www.cnblogs.com/easonliu/p/4531020.html
感觉这题算是很难的题了 ... 也是自己没有想法 ... 看题解还要想很久的题目
还是很神奇的 .. 不知道他们怎么想出来的算法

如果不维持一个有序的heap 那么每次取cur为当前最高高度时 cur = max(heap) 无疑TLE
那么我用二分法优化了插入排序 维持heap为一个有序的数组 可以AC
'''

class Solution(object):
    # :type buildings: List[List[int]]
    # :rtype: List[List[int]]
    def getSkyline(self, buildings):
        height = []
        for b in buildings:
            # 把水平线拆成左顶点和右顶点
            height.append([b[0], -b[2]])    # 左顶点的高用负数表示 来区分出它是左边顶点
            height.append([b[1], b[2]])     # 右顶点的高为正数
        height = sorted(height)     # 按x轴坐标排序
        heap, res = [0], []
        pre, cur = 0, 0     # pre表示上一轮最高度 cur表示当前最高度
        for h in height:    # 按x轴从左到右遍历
            if h[1] < 0:
                # 左顶点
                # 保证heap是一个升序的数组 heap的最后一个元素是当前维持的最高building值
                heap.insert(self.getInsertPos(heap, -h[1]), -h[1])
            else:
                # 遇到右顶点 把左顶点的高从heap消灭
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