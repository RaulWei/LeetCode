# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        version1 = '0' + version1.lstrip('0')
        version2 = '0' + version2.lstrip('0')
        if '.' not in version1:
            version1 += '.0'
        if '.' not in version2:
            version2 += '.0'
        ver_1 = version1.split('.')
        ver_2 = version2.split('.')
        if int(ver_1[0]) > int(ver_2[0]):
            return 1
        elif int(ver_1[0]) == int(ver_2[0]):
            if int(ver_1[1]) > int(ver_2[1]):
                return 1
            elif int(ver_1[1]) == int(ver_2[1]):
                return 0
            else:
                return -1
        else:
            return -1
        pass

if __name__ == '__main__':
    sol = Solution()
    print(sol.compareVersion('0.1', '1.0'))
