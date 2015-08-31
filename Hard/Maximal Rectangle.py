# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
本题算是Largest Rectangle in Histogram的进阶
求01矩阵中包含1最多的矩形
对于矩阵的每一行看作直方图 立柱的高度就是行元素往上数1的个数
最后求各行结果的最大值即可
参考 http://www.cnblogs.com/felixfang/p/3676193.html

注意 本题的输入不是[["111"], ["111"]] 而是["111", "111"]
'''

class Solution(object):
    # :type matrix: List[List[str]]
    # :rtype: int
    def maximalRectangle(self, matrix):
        max_area = 0
        for row in range(len(matrix)):
            matrix[row] += '#'
            i, stack = 0, []
            while i < len(matrix[row]):
                while stack and self.height(matrix, row, i) < self.height(matrix, row, stack[-1]):
                    tmp = stack.pop()
                    tmp_height = self.height(matrix, row, tmp)
                    # 以tmp为高度 tmp所在柱以及向左延伸出的面积
                    left_area = tmp_height * (tmp + 1 if not stack else tmp - stack[-1])
                    # 以tmp为高度 向右延伸出的面积
                    right_area = tmp_height * (i - tmp - 1)
                    area = left_area + right_area
                    max_area = area if area > max_area else max_area
                stack.append(i)
                i += 1
        return max_area

    def height(self, matrix, row, col):
        if matrix[row][col] == '#':
            return 0
        height = 0
        while row >= 0 and matrix[row][col] == '1':
            height += 1
            row -= 1
        return height


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximalRectangle(["1"]))
    print(sol.maximalRectangle(["111", "111"]))