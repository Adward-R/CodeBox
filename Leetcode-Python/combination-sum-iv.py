class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dp = [1] + [0] * target
        for i in range(1, target+1):
            j = 0
            while j < len(nums) and nums[j] <= i:
                dp[i] += dp[i - nums[j]]
                j += 1
        return dp[-1]

sol = Solution()
nums = [1,2,3]
print(sol.combinationSum4(nums, 4))