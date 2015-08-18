__author__ = 'Adward'

class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        while len(nums1) > m:
            nums1.pop()
        while len(nums2) > n:
            nums2.pop()
        nums1 += nums2
        list.sort(nums1)


sol = Solution()
nums1 = [1,0]
nums2 = [2]
sol.merge(nums1,1,nums2,1)
print(nums1)