__author__ = 'Adward'
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        S = [0]  # S[i] denotes sum(nums[0:i]), exclusively
        # so range_sum(i,j) == S[j+1]-S[i]
        for num in nums:
            S.append(S[-1] + num)

        def mergeSort(lo, hi):
            mid = (lo + hi) // 2
            if mid == lo:
                return 0
            count = mergeSort(lo, mid) + mergeSort(mid, hi)
            i = j = mid
            for left in S[lo:mid]:
                while i < hi and S[i] - left < lower:
                    i += 1
                while j < hi and S[j] - left <= upper:
                    j += 1
                count += j - i
            S[lo:hi] = sorted(S[lo:hi])
            return count

        return mergeSort(0, len(S))

sol = Solution()
nums = [-2,5,-1,-1,3,-2,4,1,2,-8]
print(sol.countRangeSum(nums, -1, 3))