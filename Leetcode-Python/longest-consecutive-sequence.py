__author__ = 'Adward'
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        adjacents = {}
        ans = 0
        for num in nums:
            if num not in adjacents:
                left = adjacents.get(num - 1, 0)
                right = adjacents.get(num + 1, 0)
                cur_length = left + right + 1
                adjacents[num] = cur_length
                # keep track of max length seen so far
                ans = max(ans, cur_length)
                # extend the cur_length to the boundary of the sequence
                adjacents[num - left] = adjacents[num + right] = cur_length
        return ans

nums = [5, 100, 4, 7, 6, 200, 1, 3, 2]
sol = Solution()
print(sol.longestConsecutive(nums))