__author__ = 'Adward'
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def bfs(visited, Q, m, n):
            while len(Q):
                newQ = []
                for i, j in Q:
                    adjacents = []
                    visited[i][j] = True
                    h = matrix[i][j]
                    if i > 0:
                        adjacents.append((i-1, j))
                    if i + 1 < m:
                        adjacents.append((i+1, j))
                    if j > 0:
                        adjacents.append((i, j-1))
                    if j + 1 < n:
                        adjacents.append((i, j+1))
                    for row, col in adjacents:
                        if not visited[row][col] and matrix[row][col] >= h:
                            newQ.append((row, col))
                Q = newQ

        try:
            m, n = len(matrix), len(matrix[0])
        except:
            return []

        pacific = [[False] * n for _ in range(m)]
        init_Q = [(i, 0) for i in range(m)] + [(0, j) for j in range(1, n)]
        bfs(pacific, init_Q, m, n)

        atlantic = [[False] * n for _ in range(m)]
        init_Q = [(i, n-1) for i in range(m)] + [(m-1, j) for j in range(n-1)]
        bfs(atlantic, init_Q, m, n)

        ans = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])
        return ans


sol = Solution()
matrix = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]
print(sol.pacificAtlantic(matrix))