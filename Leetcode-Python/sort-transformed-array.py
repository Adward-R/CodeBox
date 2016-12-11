__author__ = 'Adward'
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        if a == 0:
            if b > 0:
                return [b*x + c for x in nums]
            elif b < 0:
                return [b*x + c for x in reversed(nums)]
            else:
                return [c] * len(nums)

        # for Python 2 compatibility you should add "* 1.0"
        peak = - b * 1.0 / (2*a)
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > peak:
                right = mid
            elif nums[mid] < peak:
                left = mid
            else:
                break

        peak_pos = -1
        if left + 1 < right:
            peak_pos = (left+right) // 2
        elif nums[left] == peak:
            peak_pos = left
        elif nums[right] == peak:
            peak_pos = right

        # pl, pr = 0, 0
        reformed = []
        if peak_pos >= 0:
            reformed.append(nums[peak_pos])
            pl, pr = peak_pos-1, peak_pos+1
        else:
            pl, pr = left, right

        while pl >= 0 and pr < len(nums):
            if peak - nums[pl] <= nums[pr] - peak:
                reformed.append(nums[pl])
                pl -= 1
            else:
                reformed.append(nums[pr])
                pr += 1
        while pl >= 0:
            reformed.append(nums[pl])
            pl -= 1
        while pr < len(nums):
            reformed.append(nums[pr])
            pr += 1

        if a > 0:
            return [a*n*n + b*n + c for n in reformed]
        else:
            return [a*n*n + b*n + c for n in reversed(reformed)]

sol = Solution()
nums = [-4, -2, 2, 4]
print(sol.sortTransformedArray(nums, -1, 3, 5))