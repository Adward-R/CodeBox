class Solution(object):
    def countDigitOne2(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        for i in range(1, n+1):
        	s = str(i)
        	for ch in s:
        		if ch == '1':
        			cnt += 1
        	if cnt != self.countDigitOne2(i):
        		print(i)
#        	print(str(i)+'|'+str(cnt)+'|'+str(self.countDigitOne2(i)))
        #print(self.countDigitOneRange1000(n))
        return cnt

    def countDigitOne(self, n):
    	leng = len(str(n))
    	cnt = 0
    	for i in range(leng):
    		limit = 10**i
    		tail = (n % (10 * limit)) - limit + 1
    		body = (n / (10 * limit))
    		
    		if tail >= limit:
    			tail = limit
    		elif tail < 0:
    			tail = 0
    		cnt += limit * body + tail
    	return cnt

sol = Solution()
print(sol.countDigitOne(61005))
