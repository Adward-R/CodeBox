__author__ = 'Adward'
class Solution(object):
    def findMinIdx(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        elif n == 2:
            if nums[0] > nums[1]:
                return 1
            else:
                return 0

        left = 0
        right = n - 1
        while left + 1 < right:
            mid = int((left + right) / 2)
            if nums[mid] > nums[mid+1]:
                return mid+1
            else:
                if nums[mid] > nums[right]:
                    left = mid
                else:
                    right = mid
        for i in range(left, right+1):
            if nums[i] > nums[i+1]:
                return i+1
        return 0

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        minIdx = self.findMinIdx(nums)
        nums = nums[minIdx:] + nums[0:minIdx]
        try:
            idx = nums.index(target)
            return (minIdx + idx) % len(nums)
        except:
            return -1

sol = Solution()
#nums = [4,5,6,7,0,1,2]
nums = []
print(sol.search(nums, 4))