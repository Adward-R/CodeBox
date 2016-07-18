__author__ = 'Adward'
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        linkage = [[] for i in range(n)]
        for e in edges:
            linkage[e[0]].append(e[1])
            linkage[e[1]].append(e[0])
        traversed = [True] + [False] * (n-1)
        q = [(None, 0)]
        while len(q):
            lenq = len(q)
            for i in range(lenq):
                for node in linkage[q[i][1]]:
                    if node != q[i][0]:
                        q.append((q[i][1], node))
                        if not traversed[node]:
                            traversed[node] = True
                        else:
                            return False
            q = q[lenq:]
        for status in traversed:
            if not status:
                return False
        return True

sol = Solution()
# edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
edges = [[0,1], [2,3]]
print(sol.validTree(4, edges))