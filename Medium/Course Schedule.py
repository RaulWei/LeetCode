# -*- coding: UTF-8 -*-
__author__ = 'wang'

class Solution(object):
    # :type numCourses: int
    # :type prerequisites: List[List[int]]
    # :rtype: bool
    def canFinish(self, numCourses, prerequisites):
        in_degree, next = dict(), dict()
        for edge in prerequisites:
            if edge[0] not in in_degree:
                in_degree[edge[0]] = 0
            if edge[1] not in in_degree:
                in_degree[edge[1]] = 1
            else:
                in_degree[edge[1]] += 1
            if edge[0] not in next:
                next[edge[0]] = [edge[1]]
            else:
                next[edge[0]].append(edge[1])
        while in_degree:
            find = False
            for key in in_degree:
                if in_degree[key] == 0:
                    if key in next:
                        for nx in next[key]:
                            in_degree[nx] -= 1
                    in_degree.pop(key)
                    find = True
                    break
            if not find:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.canFinish(2, [[1,0]]))
    print(sol.canFinish(2, [[1,0],[0,1]]))