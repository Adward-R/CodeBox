class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        rgs = []
        leng = len(nums)
        if leng == 0:
        	return rgs
        left = nums[0]
        for i in range(leng):
        	if i+1 == leng or nums[i+1]-nums[i] != 1:
        		if left != nums[i]:
	        		rgs.append(str(left) + '->' + str(nums[i]))
	        	else:
	        		rgs.append(str(left))
	        	try:
	        		left = nums[i+1]
	        	except:
	        		pass
      	return rgs

sol = Solution()
print(sol.summaryRanges([-5,-4,-3,0]))