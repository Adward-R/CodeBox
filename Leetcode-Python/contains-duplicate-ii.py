class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) <= 0 or k <= 0:
        	return False
        mmax = nums[0]
        mmin = nums[0]
        for n in nums:
        	if n > mmax:
        		mmax = n
        	if n < mmin:
        		mmin = n
        #llst = [[]] * (mmax-mmin+1)
        llst = []
        for i in range(mmax-mmin+1):
        	llst.append([])

        idx = 0
        for n in nums:
        	llst[n-mmin].append(idx)
        	idx += 1
        print(llst)
        for lst in llst:
        	for i in range(len(lst)-1):
        		lst[i] = lst[i+1] - lst[i]
	        	if lst[i] > 0 and lst[i] <= k:
	        		return True
        return False

sol = Solution()
lst = []
for i in range(30000):
	lst.append(i)
print(sol.containsNearbyDuplicate([1,0,1,1], 1))