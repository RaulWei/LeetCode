# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
拓扑排序的前身是判断有向图是否存在环
本题就是判断有向图是否存在环的问题
'''

class Solution(object):
    # :type numCourses: int
    # :type prerequisites: List[List[int]]
    # :rtype: bool
    def canFinish(self, numCourses, prerequisites):
        in_degree, next = dict(), dict()    # 构建入度字典 key为节点值 value为入度; 构建next字典 key为当前节点 value连接的节点们
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
            # 找到入度为0的节点 POP 继续找
            # 如果找不到入度为0的节点 说明存在有向图的环 返回False
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