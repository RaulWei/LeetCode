# -*- coding: UTF-8 -*-
__author__ = 'wang'

class Solution(object):
    # :type gas: List[int]
    # :type cost: List[int]
    # :rtype: int
    def canCompleteCircuit(self, gas, cost):
        lens, start_index = len(gas), 0
        while start_index < lens:
            step, left_gas, find = 0, 0, True
            while step < lens:
                left_gas += gas[(start_index + step) % lens] - cost[(start_index + step) % lens]
                if left_gas < 0:
                    find = False
                    start_index += step % lens
                    if start_index >= lens:
                        return -1
                    break
                step += 1
            if find is True:
                return start_index
            start_index += 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.canCompleteCircuit([4], [5]))
    print(sol.canCompleteCircuit([1, 2, 3], [1, 2, 3]))