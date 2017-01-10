__author__ = 'Adward'
class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def minDist1D(nums, n_points):
            onLeft = i = 0
            while i < len(nums):
                if onLeft + nums[i] >= n_points - onLeft - nums[i]:
                    break
                onLeft += nums[i]
                i += 1
            return sum([abs(i-j) * nums[j] for j in range(len(nums))])

        vertical_proj = [sum(grid[i]) for i in range(len(grid))]
        n_people = sum(vertical_proj)
        horizon_proj = [sum([grid[i][j] for i in range(len(grid))]) for j in range(len(grid[0]))]
        return minDist1D(vertical_proj, n_people) + minDist1D(horizon_proj, n_people)