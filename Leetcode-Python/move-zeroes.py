__author__ = 'Adward'
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        leng = len(nums)
        zeros = 0
        for i in range(leng):
            if nums[i] == 0:
                zeros += 1
            else:
                nums[i-zeros] = nums[i]
        for i in range(leng-zeros, leng):
            nums[i] = 0

sol = Solution()
nums = [0,1,2,0,3,0]
sol.moveZeroes(nums)
print(nums)