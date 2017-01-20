__author__ = 'Adward'
class Solution(object):
    # 0/1 Knapsack Problem
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2:
            return False
        half = total // 2

        dp = [True] + [False] * half
        for num in nums:
            i = half
            while i >= num:
                # take i-th num: dp[i][j] = dp[i-1][j]; not take: dp[i][j] = dp[i-1][j-nums[i]]
                dp[i] |= dp[i-num]
                i -= 1
        return dp[-1]