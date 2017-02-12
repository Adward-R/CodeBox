from heapq import *
class Solution(object):
    def trapRainWater(self, heightMap):  # BFS
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        volume = 0
        m = len(heightMap) if heightMap else 0
        if m == 0:
            return 0
        n = len(heightMap[0])
        if n == 0:
            return 0
        visited = [[False] * n for _ in range(m)]

        pq = []
        # Initially, add all the Cells which are on borders to the queue.
        for i in range(m):
            visited[i][0] = visited[i][n-1] = True
            heappush(pq, (heightMap[i][0], i, 0))
            heappush(pq, (heightMap[i][n-1], i, n-1))
        for j in range(1, n-1):
            visited[0][j] = visited[m-1][j] = True
            heappush(pq, (heightMap[0][j], 0, j))
            heappush(pq, (heightMap[m-1][j], m-1, j))


        # From the borders, pick the shortest cell visited and check its neighbors:
        # if the neighbor is shorter, collect the water it can trap,
        # and update its height as (its height + the water trapped) & add all its neighbors to the queue.
        while len(pq):
            h, x, y = heappop(pq)
            for dx, dy in dirs:
                row, col = x + dx, y + dy
                if 0 <= row < m and 0 <= col < n and not visited[row][col]:
                    visited[row][col] = True  # don't have to really update heightMap
                    volume += max(0, h - heightMap[row][col])
                    heappush(pq, (max(h, heightMap[row][col]), row, col))

        return volume

sol = Solution()
heightMap = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]
print(sol.trapRainWater(heightMap))