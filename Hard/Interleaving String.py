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
        flag = [[1 for col in range(len(s2) + 1)] for row in range(len(s1) + 1)]
        return self.DFS(0, s1, 0, s2, 0, s3, s, flag)

    def DFS(self, step, s1, idx_1, s2, idx_2, s3, s, flag):
        if step == len(s3):
            return True

        print(idx_1)
        print(idx_2)
        print(s3[:len(s) + 1])

        # check s1
        if idx_1 < len(s1) and s + s1[idx_1] == s3[:len(s) + 1]:
            s += s1[idx_1]
            if flag[idx_1][idx_2] == 1 and self.DFS(step + 1, s1, idx_1 + 1, s2, idx_2, s3, s, flag):
                return True
            s = s.rstrip(s1[idx_1])
            flag[idx_1 + 1][idx_2] = 0
        # check s2
        if idx_2 < len(s2) and s + s2[idx_2] == s3[:len(s) + 1]:
            s += s2[idx_2]
            if flag[idx_1][idx_2] == 1 and self.DFS(step + 1, s1, idx_1, s2, idx_2 + 1, s3, s, flag):
                return True
            s = s.rstrip(s2[idx_2])
            flag[idx_1][idx_2 + 1] = 0

        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.isInterleave("aabd", "abdc", "aabdabcd"))
    # print(sol.isInterleave("a", "a", "aa"))
    # print(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
    # print(sol.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
    # print(sol.isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa", "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"))