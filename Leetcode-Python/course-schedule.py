__author__ = 'Adward'
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjaLst = []
        indegree = [0] * numCourses
        for i in range(numCourses):
            adjaLst.append([])
        for edge in prerequisites:
            adjaLst[edge[1]].append(edge[0])
            indegree[edge[0]] += 1

        topOrder = []
        q = []
        cnt = 0
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while len(q):
            cnt += 1
            topOrder.append(q[0])
            q = q[1:]
            for v in adjaLst[topOrder[-1]]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        if cnt != numCourses:
            return False
        else:
            return True

sol = Solution()
print(sol.canFinish(2, [[1,0], [0,1]]))