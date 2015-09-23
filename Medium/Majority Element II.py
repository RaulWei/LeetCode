# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
找到所有出现次数超过 N/3次的数 这样的数肯定不会超过两个吧
'''

class Solution(object):
    # :type nums: List[int]
    # :rtype: List[int]
    def majorityElement(self, nums):
        if not nums:
            return []
        candidate_1, candidate_2, candidate_1_num, candidate_2_num = 0, 1, 0, 0
        for n in nums:
            if n == candidate_1:
                candidate_1_num += 1
            elif n == candidate_2:
                candidate_2_num += 1
            elif candidate_1_num == 0:
                candidate_1, candidate_1_num = n, 1
            elif candidate_2_num == 0:
                candidate_2, candidate_2_num = n, 1
            else:
                candidate_1_num -= 1
                candidate_2_num -= 1
        return [n for n in (candidate_1, candidate_2) if nums.count(n) > len(nums) / 3]

if __name__ == '__main__':
    sol = Solution()
    print(sol.majorityElement([2, 2, 9, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9]))