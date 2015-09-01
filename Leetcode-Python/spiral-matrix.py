__author__ = 'Adward'

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])

        flags = []
        for i in range(m):
            flags.append([1] * n)

        x = 0
        y = 0
        direction = 0 # -> down <- up
        res = []

        try:
            while flags[y][x]:
                #print(str(y) + ':' + str(x))
                flags[y][x] = 0
                res.append(matrix[y][x])
                if direction == 0:
                    if x+1 < n and flags[y][x+1]:
                        x += 1
                    else:
                        direction = 1
                        y += 1
                elif direction == 1:
                    if y+1 < m and flags[y+1][x]:
                        y += 1
                    else:
                        direction = 2
                        x -= 1
                elif direction == 2:
                    if x > 0 and flags[y][x-1]:
                        x -= 1
                    else:
                        direction = 3
                        y -= 1
                else:
                    if y > 0 and flags[y-1][x]:
                        y -= 1
                    else:
                        direction = 0
                        x += 1
        except:
            pass

        return res

sol = Solution()
print(sol.spiralOrder([
    [1],
    [2],
    [3]
]))