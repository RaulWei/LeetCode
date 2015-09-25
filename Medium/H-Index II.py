# -*- coding: UTF-8 -*-
__author__ = 'wang'

class Solution(object):
    # :type citations: List[int]
    # :rtype: int
    def hIndex(self, citations):
        length = len(citations)
        for i in range(length)[::-1]:
            if length - i >= citations[i]:
                return citations[i]
        return 0


