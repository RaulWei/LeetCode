# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
基于一个事实：如果A到达不了B（B是第一个A到达不了的节点） 那么AB之间以任何节点为start都到达不了B
'''

class Solution(object):
    # :type gas: List[int]
    # :type cost: List[int]
    # :rtype: int
    def canCompleteCircuit(self, gas, cost):
        lens, start_index = len(gas), 0
        while start_index < lens:   # 枚举start_index
            step, left_gas, find = 0, 0, True
            while step < lens:
                left_gas += gas[(start_index + step) % lens] - cost[(start_index + step) % lens]
                if left_gas < 0:    # 到达不了B点
                    find = False
                    start_index += step % lens  # 更新start_index到B点
                    break
                step += 1
            if find is True:    # 找到start_index直接返回 题目说本题只有一个合法的解决方案
                return start_index
            start_index += 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.canCompleteCircuit([4], [5]))
    print(sol.canCompleteCircuit([1, 2, 3], [1, 2, 3]))