__author__ = 'Adward'
import random
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid
            else:
                hi -= 1
        return nums[lo]


sol = Solution()
'''
print(sol.findMin([3,3,3,3,3,3,3,3,1,3]))
print(sol.findMin([1,1,1]))
print(sol.findMin([3,1,1]))
print(sol.findMin([3,3,1,2,2,2]))
print(sol.findMin([1,1,3,3,3]))
'''
def genRandLst():
    ns = int(random.random()*100) % 5 + 1
    lst = []
    for i in range(1, ns+1):
        for j in range(int(random.random()*100) % 5 + 1):
            lst.append(i)
    pivot = int(random.random()*1000) % len(lst)
    lst = lst[pivot:] + lst[:pivot]
    return lst

for i in range(1000):
    lst = genRandLst()
    res = sol.findMin(lst)
    if res != min(lst):
        print(str(lst)+' | '+ res)