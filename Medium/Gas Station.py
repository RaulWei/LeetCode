# -*- coding: UTF-8 -*-
__author__ = 'wang'

class Solution(object):
    # :type gas: List[int]
    # :type cost: List[int]
    # :rtype: int
    def canCompleteCircuit(self, gas, cost):
        lens = len(gas)
        for start_index in range(lens):
            step, left_gas, find = 0, 0, True
            while step < lens:
                left_gas += gas[step % lens] - cost[step % lens]
                if left_gas < 0:
                    find = False
                    break
                step += 1
            if find is True:
                return start_index
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.canCompleteCircuit([4], [5]))
    print(sol.canCompleteCircuit([1, 2, 3], [1, 2, 3]))