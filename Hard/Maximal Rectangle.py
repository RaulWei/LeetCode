# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
本题算是Largest Rectangle in Histogram的进阶
求01矩阵中包含1最多的矩形
对于矩阵的每一行看作直方图 立柱的高度就是行元素往上数1的个数
'''

class Solution(object):
    # :type matrix: List[List[str]]
    # :rtype: int
    def maximalRectangle(self, matrix):
        max_area = 0
        for row in range(len(matrix)):
            matrix[row].append(-1)
            left_area, right_area = 0, 0
            i, stack = 0, []
            while i < len(matrix[row]):
                while stack and self.height(matrix, row, i) < self.height(matrix, row, stack[-1]):
                    tmp = stack.pop()
                    left_area = self.height(matrix, row, tmp) * (tmp + 1 if not stack else tmp - stack[-1])   # 以tmp为高度 tmp所在柱以及向左延伸出的面积
                    right_area = self.height(matrix, row, tmp) * (i - tmp - 1)    # 以tmp为高度 向右延伸出的面积
                    area = left_area + right_area
                    max_area = area if area > max_area else max_area
                stack.append(i)
                i += 1
        return max_area

    def height(self, matrix, row, col):
        if matrix[row][col] == -1:
            return 0
        height = 0
        while row >= 0 and matrix[row][col] == 1:
            height += 1
            row -= 1
        return height


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximalRectangle([["111"], ["111"]]))