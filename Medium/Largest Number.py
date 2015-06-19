# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
定义两个数的大小标准
a和b 如果ab>ba 那么a>b
比如3和30 330>303 所以3>30
'''

class Solution:
    def cmp(self, a, b):
        if int(str(a) + str(b)) > int(str(b) + str(a)):
            # 认为a>b
            return 1
        else:
            return -1

    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums.sort(cmp=self.cmp, reverse=True)
        ret = ''.join(str(x) for x in nums).lstrip('0')
        if not ret:
            # 考虑可能有nums=[0, 0, 0 ...]的情况
            return '0'
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.largestNumber([3, 30, 34, 5, 9]))
