# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
一开始的想法是遍历每个长方形 向左向右扩展找最大 结果超时
实在是想不出有什么更好的办法
参考 http://www.cnblogs.com/felixfang/p/3676193.html 构造递增
'''

class Solution(object):
    # :type height: List[int]
    # :rtype: int
    def largestRectangleArea(self, height):
        height.append(0)
        left_area, right_area, max_area = 0, 0, 0
        i, stack = 0, []
        while i < len(height):
            while stack and height[i] < height[stack[-1]]:
                tmp = stack.pop()
                left_area = height[tmp] * (tmp + 1 if not stack else tmp - stack[-1])   # 以tmp为高度 tmp所在柱以及向左延伸出的面积
                right_area = height[tmp] * (i - tmp - 1)    # 以tmp为高度 向右延伸出的面积
                area = left_area + right_area
                max_area = area if area > max_area else max_area
            stack.append(i)
            i += 1
        return max_area

if __name__ == '__main__':
    sol = Solution()
    print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))
