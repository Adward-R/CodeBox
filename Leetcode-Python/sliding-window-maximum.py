__author__ = 'Adward'
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k <= 1:
            return nums
        deq = [nums[0]]
        mmax = nums[0]
        for i in range(1, k):
            num = nums[i]
            if num >= mmax:
                deq = [num]
                mmax = num
            else:
                deq.append(num)

        maxs = [mmax]
        for i in range(k, len(nums)):
            print(deq)
            num = nums[i]
            if num >= mmax:
                deq = [num]
                mmax = num
            else:
                deq.append(num)
                if len(deq) >= k+1:
                    tmp = deq[0]
                    deq = deq[1:]
                    if tmp == mmax:
                        mmax = max(deq)
            maxs.append(mmax)
        return maxs

sol = Solution()
#print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(sol.maxSlidingWindow([1,2,3,4,2],3))