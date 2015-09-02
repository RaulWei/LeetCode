# -*- coding: UTF-8 -*-
__author__ = 'wang'

class Solution(object):
    # :type s1: str
    # :type s2: str
    # :rtype: bool
    def isScramble(self, s1, s2):
        if s1 == s2:
            return True

        # 剪枝 各字母数不同 可直接return False
        alphabet = [0 for col in range(128)]
        for i in range(len(s1)):
            alphabet[ord(s1[i])] += 1
        for i in range(len(s2)):
            alphabet[ord(s2[i])] -= 1
        for col in range(128):
            if alphabet[col] != 0:
                return False

        # 递归
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:len(s1)], s2[i:len(s2)])):
                return True
            if self.isScramble(s1[:i], s2[i:]) and self.isScramble(s1[i:], s2[:i]):
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.isScramble("abb", "bba"))
    print(sol.isScramble("great", "rgeat"))
    print(sol.isScramble("great", "rgtae"))