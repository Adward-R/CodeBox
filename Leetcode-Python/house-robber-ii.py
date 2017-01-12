__author__ = 'Adward'
class Solution(object):
    def rob_helper(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        pprevMax, prevMax = nums[0], max(nums[0:2])
        for i in range(2, len(nums)):
            pprevMax, prevMax = prevMax, max(nums[i] + pprevMax, prevMax)
        return prevMax

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(self.rob_helper(nums[0:-1]), self.rob_helper(nums[1:]))




sol = Solution()
lst = [
    # [5,3,1,2,4,1,6,8,9],
    # [1,2,1,0],
    # [1,1,1],
    # [2,3,2],
    # [2,2,4,3,2,5],
    [55,72,209,143,216,220,122,115,87,227,220,161,79,230,55,56,56,178,124,88,202,65,102]
]
for nums in lst:
    print(sol.rob(nums))
