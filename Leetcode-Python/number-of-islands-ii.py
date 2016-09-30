__author__ = 'Adward'
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        grid = [[0] * n for i in range(m)]
        num_of_islands = []
        labels = []
        last_label = 0

        for x, y in positions:
            adjacent_labels = set()
            if x > 0 and grid[x-1][y]:
                adjacent_labels.add(grid[x-1][y])
            if x < m - 1 and grid[x+1][y]:
                adjacent_labels.add(grid[x+1][y])
            if y > 0 and grid[x][y-1]:
                adjacent_labels.add(grid[x][y-1])
            if y < n - 1 and grid[x][y+1]:
                adjacent_labels.add(grid[x][y+1])

            if len(adjacent_labels) == 0:
                last_label += 1
                grid[x][y] = last_label
                labels.append({last_label})
            elif len(adjacent_labels) == 1:
                grid[x][y] = list(adjacent_labels)[0]
            else:
                grid[x][y] = list(adjacent_labels)[0]
                equivalents = []
                for i in range(len(labels)):
                    for lbl in adjacent_labels:
                        if lbl in labels[i]:
                            equivalents.append(i)
                            break
                new_set = labels[equivalents[0]]
                for k in equivalents[1:]:
                    new_set = new_set.union(labels[k])
                labels[equivalents[0]] = new_set
                for k in equivalents[:0:-1]:
                    labels.pop(k)
            num_of_islands.append(len(labels))
        return num_of_islands

sol = Solution()
positions = [[0,5],[5,4],[5,2],[7,3],[6,0],[5,3],[5,1],[1,3],[4,3],[2,3],[3,5],[3,2],[3,0],[2,4],[0,1]]
print(sol.numIslands2(8, 6, positions))