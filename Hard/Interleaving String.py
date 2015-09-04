# -*- coding: UTF-8 -*-
__author__ = 'weimw'

class Solution(object):
    # :type s1: str
    # :type s2: str
    # :type s3: str
    # :rtype: bool
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        s = ''
        return self.DFS(0, s1, 0, s2, 0, s3, s)

    def DFS(self, step, s1, idx_1, s2, idx_2, s3, s):
        if step == len(s3):
            return True

        # check s1
        if idx_1 < len(s1) and s3.find(s + s1[idx_1]) != -1:
            s += s1[idx_1]
            if not self.DFS(step + 1, s1, idx_1 + 1, s2, idx_2, s3, s):
                s = s.rstrip(s1[idx_1])
            else:
                return True
        # check s2
        if idx_2 < len(s2) and s3.find(s + s2[idx_2]) != -1:
            s += s2[idx_2]
            if not self.DFS(step + 1, s1, idx_1, s2, idx_2 + 1, s3, s):
                s = s.rstrip(s2[idx_2])
            else:
                return True
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
    print(sol.isInterleave("aabcc", "dbbca", "aadbbbaccc"))