# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
leetcode上中等难度的题基本写出来就差不多能过了
BFS一下搞定
'''

class Solution(object):
    # :type grid: List[List[str]]
    # :rtype: int
    def numIslands(self, grid):
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        island_num = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.BFS(i, j, grid, row, col)
                    island_num += 1
        return island_num

    def BFS(self, row, col, grid, row_num, col_num):
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 上 下 左 右
        queue = [[row, col]]
        while queue:
            cur = queue.pop(0)
            x, y = cur[0], cur[1]
            grid[x] = "".join(grid[x][:y]) + 'T' + "".join(grid[x][y + 1:])
            for dire in direction:
                new_x, new_y = x + dire[0], y + dire[1]
                if 0 <= new_x < row_num and 0 <= new_y < col_num and grid[new_x][new_y] == '1':
                    queue.append([new_x, new_y])
                    grid[new_x] = "".join(grid[new_x][:new_y]) + 'T' + "".join(grid[new_x][new_y + 1:])

if __name__ == '__main__':
    sol = Solution()
    print(sol.numIslands(["10011101100000000000","10011001000101010010","00011110101100001010","00011001000111001001","00000001110000000000","10000101011000000101","00010001010101010101","00010100110101101110","00001001100001000101","00100100000100100010","10010000000100101010","01000101011011101100","11010000100000010001","01001110001111101000","00111000110001010000","10010100001000101011","10100000010001010000","01100011101010111100","01000011001010010011","00000011110100011000"]))
    print(sol.numIslands(["11"]))
    print(sol.numIslands(["11110", "11010", "11000", "00000"]))
    print(sol.numIslands(["11000", "11000", "00100", "00011"]))

