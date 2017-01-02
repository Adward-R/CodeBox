__author__ = 'Adward'
import heapq
from collections import deque
class Solution(object):
    def maxNumber0(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        maxes1, maxes2 = [len(nums1)-1], [len(nums2)-1]
        for i in range(len(nums1)-2, -1, -1):
            if nums1[i] >= nums1[maxes1[-1]]:
                maxes1.append(i)
            else:
                maxes1.append(maxes1[-1])
        for i in range(len(nums2)-2, -1, -1):
            if nums2[i] >= nums2[maxes2[-1]]:
                maxes2.append(i)
            else:
                maxes2.append(maxes2[-1])
        maxes1.reverse(), maxes2.reverse()

        print(maxes1, maxes2)

        digits = []
        p1, p2 = 0, 0
        for i in range(k):
            if nums1[maxes1[p1]] > nums2[maxes2[p2]] and len(nums1)+len(nums2)-maxes1[p1]-p2 >= k-len(digits):
                p1 = maxes1[p1]
                digits.append(nums1[p1])
                p1 += 1
            elif nums1[maxes1[p1]] < nums2[maxes2[p2]] and len(nums1)+len(nums2)-maxes2[p2]-p1 >= k-len(digits):
                p2 = maxes2[p2]
                digits.append(nums2[p2])
                p2 += 1

            if p1 == len(nums1) or p2 == len(nums2):
                break

        leftLen = k - len(digits)
        if leftLen:
            if p1 == len(nums1):
                digits += nums2[p2:]
            else:
                digits += nums1[p1:]
        return digits

    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        def mergeMax(left, right):
            ret = []
            while left or right:
                ret.append(left.popleft() if left > right else right.popleft())
            return ret

        def maxKSelect(nums, k):
            n = len(nums)
            ret = [-1]
            if k > n:
                return deque(ret)
            for i in range(k, 0, -1):
                ret.append(max(range(ret[-1]+1, n-i+1), key=nums.__getitem__))
            return deque([nums[ind] for ind in ret[1:]])

        m, n = len(nums1), len(nums2)
        ans = [0] * k
        for i in range(0, k+1):
            j = k - i
            if i > m or j > n:
                continue
            num = mergeMax(maxKSelect(nums1, i), maxKSelect(nums2, j))
            ans = max(num, ans)
        return ans


sol = Solution()
nums1 = [2,5,6,4,4,0]
nums2 = [7,3,8,0,6,5,7,6,2]
print(sol.maxNumber(nums1, nums2, 15))
# print(sol.maxNumber([1,1], [1], 3))