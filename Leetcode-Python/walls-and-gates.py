__author__ = 'Adward'
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        # INF = 1 << 31 - 1
        try:
            m, n = len(rooms), len(rooms[0])
        except:
            return
        doors = [(i, j) for j in range(n) for i in range(m) if rooms[i][j] == 0]

        for door in doors:
            Q = [door]
            curLength = 0
            while len(Q):
                newQ = []
                for i, j in Q:
                    rooms[i][j] = min(curLength, rooms[i][j])
                    if i > 0 and rooms[i-1][j] > curLength+1:
                        newQ.append((i-1, j))
                    if i < m-1 and rooms[i+1][j] > curLength+1:
                        newQ.append((i+1, j))
                    if j > 0 and rooms[i][j-1] > curLength+1:
                        newQ.append((i, j-1))
                    if j < n-1 and rooms[i][j+1] > curLength+1:
                        newQ.append((i, j+1))
                Q = newQ
                curLength += 1

INF = 2147483647
sol = Solution()
rooms = [
    [INF, -1, 0, INF],
    [INF, INF, INF, -1],
    [INF, -1, INF, -1],
    [0, -1, INF, INF]
]
sol.wallsAndGates(rooms)
for row in rooms:
    print(row)