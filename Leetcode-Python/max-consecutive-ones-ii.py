class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = -1
        max_conseq = 1
        last_s = last_e = -1
        n = len(nums)
        
        for e in range(n+1):
            if e < n and nums[e]:
                if s < 0:
                    s = e
            else:
                if s >= 0:  # (e-s)+1 cuz can still flip one when there's no linked conseq 1s (if e-s+1 <= n)
                    max_conseq = max(max_conseq, 
                        e - last_s if last_s >= 0 else min(e-s+1, n))  
                    last_s, last_e = s, e-1
                    s = -1
                else:
                    if e - last_e > 1:
                        last_s = last_e = -1
        return max_conseq
                    