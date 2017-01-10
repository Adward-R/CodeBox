__author__ = 'Adward'
class Solution(object):
    def minCost0(self, costs):  # costs: n x 3
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        N = len(costs)  # num of houses
        if N < 1:
            return 0
        # DP[i][j] indicates (minCost, leftColor, rightColor) between house [i,j]
        DP = [[None] * N for _ in range(N)]
        for i in range(N):  # boundary
            color = min(range(3), key=lambda x: costs[i][x])
            DP[i][i] = (costs[i][color], color, color)
        for w in range(2, N+1):  # width
            for i in range(N+1-w):
                j = i + w - 1
                # ->
                minCostLeft, oldLeftColor, rightColor = DP[i][j-1]
                colors = sorted(range(3), key=lambda c: costs[j][c])
                newRightColor = colors[0] if colors[0] != rightColor else colors[1]
                minCostLeft += costs[j][newRightColor]
                # <-
                minCostRight, leftColor, oldRightColor = DP[i+1][j]
                colors = sorted(range(3), key=lambda c: costs[i][c])
                newLeftColor = colors[0] if colors[0] != leftColor else colors[1]
                minCostRight += costs[i][newLeftColor]
                #
                if minCostLeft < minCostRight:
                    DP[i][j] = (minCostLeft, oldLeftColor, newRightColor)
                else:
                    DP[i][j] = (minCostRight, newLeftColor, oldRightColor)
        return DP[0][N-1][0]

    def minCost(self, costs):  # costs: n x 3
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or len(costs) == 0:
            return 0
        N = len(costs)
        # use costs for DP: costs[i][c] -> min prices till now to paint house[i] as color c
        for i in range(1, N):
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])
            costs[i][1] += min(costs[i-1][0], costs[i-1][2])
            costs[i][2] += min(costs[i-1][0], costs[i-1][1])
        return min(costs[-1])

    def minCostII(self, costs):  # costs: n x k
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or len(costs) == 0:
            return 0
        n, k = len(costs), len(costs[0])
        # use costs for DP: costs[i][c] -> min prices till now to paint house[i] as color c
        for i in range(1, n):
            for c in range(k):
                costs[i][c] += min([costs[i-1][j] for j in range(k) if j != c])
        return min(costs[-1])

sol = Solution()
costs = [[17,15,10],[16,2,17],[14,8,15],[5,4,15],[16,1,2],
         [8,20,1],[15,20,16],[7,3,14],[1,14,15],[17,3,11],
         [16,12,18],[12,20,16],[20,2,10],[19,13,10],[1,18,8]]
print(sol.minCostII(costs))