# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        res, maxleft, maxright, left, right = 0, 0, 0, 0, len(height) - 1
        while left <= right:
            
