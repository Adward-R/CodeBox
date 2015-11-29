__author__ = 'Adward'
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        elif n == 2:
            if nums[0] < nums[1]:
                return 1
            else:
                return 0

        left = 0
        right = n - 1
        while left + 1 < right:
            mid = int((left + right) / 2)
            if nums[mid] > nums[mid+1]:
                if nums[mid] > nums[mid-1]:
                    return mid
                else:
                    right = mid
            else:
                left = mid

        for i in range(left, right+1):
            if i == 0 and nums[0] > nums[1]:
                return 0
            elif i == n-1 and nums[n-1] > nums[n-2]:
                return n-1
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i

sol = Solution()
print(sol.findPeakElement([1,2,3]))