__author__ = 'Adward'
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return min(nums)

        left = 0
        right = n - 1
        while left + 1 < right:
            mid = int((left + right) / 2)
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            else:
                if nums[mid] > nums[right]:
                    left = mid
                else:
                    right = mid

        for i in range(left, right+1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        return nums[0]


sol = Solution()
print(sol.findMin([2,3,4]))