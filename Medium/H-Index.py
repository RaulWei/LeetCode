# -*- coding: UTF-8 -*-
__author__ = 'wang'

import collections

class Solution(object):
    # :type citations: List[int]
    # :rtype: int
    def hIndex(self, citations):
        bucket = collections.defaultdict(int)   # 基于桶的排序
        for c in citations:
            for i in range(c + 1):
                bucket[i] += 1
        ret = 0
        for key in bucket:
            if bucket[key] >= key:
                ret = key
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.hIndex([1, 1]))   # 返回1 有1篇paper至少被引用1次
    print(sol.hIndex([3, 0, 6, 1, 5]))  # 返回3 有3篇paper至少被引用3次