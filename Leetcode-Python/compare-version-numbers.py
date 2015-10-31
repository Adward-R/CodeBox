class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]
        leng = len(v1)
        diff = len(v1) - len(v2)
        if diff > 0:
			for i in range(diff):
				v2.append(0)
        elif diff < 0:
			leng -= diff
			for i in range(-diff):
				v1.append(0)

        for i in range(leng):
        	if v1[i] > v2[i]:
        		return 1
        	elif v1[i] < v2[i]:
        		return -1
        return 0

sol = Solution()
print(sol.compareVersion('1.0', '1'))


