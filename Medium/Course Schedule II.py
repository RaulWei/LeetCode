# -*- coding: UTF-8 -*-
__author__ = 'wang'

class Solution(object):
    # :type numCourses: int
    # :type prerequisites: List[List[int]]
    # :rtype: List[int]
    def findOrder(self, numCourses, prerequisites):
        ret = []
        in_degree, next = dict(), dict()    # 构建入度字典 key为节点值 value为入度; 构建next字典 key为当前节点 value连接的节点们
        for point in range(numCourses):
            in_degree[point] = 0
        for edge in prerequisites:
            in_degree[edge[1]] += 1
            if edge[0] not in next:
                next[edge[0]] = [edge[1]]
            else:
                next[edge[0]].append(edge[1])
        while in_degree:
            # 找到入度为0的节点 POP 继续找
            # 如果找不到入度为0的节点 说明存在有向图的环 返回False
            find = False
            for key in in_degree:
                if in_degree[key] == 0:
                    if key in next:
                        for nx in next[key]:
                            in_degree[nx] -= 1
                    ret.append(key)
                    in_degree.pop(key)
                    find = True
                    break
            if not find:
                return []
        return ret[::-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
