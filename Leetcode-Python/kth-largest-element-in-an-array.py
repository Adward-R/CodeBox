__author__ = 'Adward'
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mmin = min(nums)
        mmax = max(nums)
        box = [0] * (mmax - mmin + 1)
        for n in nums:
            box[n-mmin] += 1
        print(box)
        cnt = 0
        i = mmax - mmin
        while i >= 0:
            if cnt < k <= cnt + box[i]:
                return i+mmin
            else:
                cnt += box[i]
                i -= 1

sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4,5], 4))