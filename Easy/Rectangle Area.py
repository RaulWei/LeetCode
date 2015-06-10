__author__ = 'Wang'

class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        # 两个矩形面积相加减去相交部分面积
        area_1 = self.computeRectArea(A, B, C, D)
        area_2 = self.computeRectArea(E, F, G, H)
        l_d_x = max(A, E)
        l_d_y = max(B, F)
        r_u_x = min(C, G)
        r_u_y = min(D, H)
        area_3 = 0
        if l_d_x <= r_u_x and l_d_y <= r_u_y:
            # 判断相交
            area_3 = self.computeRectArea(l_d_x, l_d_y, r_u_x, r_u_y)
        return area_1 + area_2 - area_3

    def computeRectArea(self, l_d_x, l_d_y, r_u_x, r_u_y):
        # 给定左下角坐标和右上角坐标 计算矩形面积
        x = r_u_x - l_d_x
        y = r_u_y - l_d_y
        return x * y

if __name__ == '__main__':
    sol = Solution()
    print(sol.computeArea(-3,0,3,4,0,-1,9,2))