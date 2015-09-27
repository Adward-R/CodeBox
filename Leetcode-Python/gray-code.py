__author__ = 'Adward'

class Solution(object):
    def bits2decimal(self, bits):
        res = 0
        for b in bits:
            res = res * 2 + int(b)
        return res
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n <= 0:
            return [0]
        ss = ['0', '1']
        halfLeng = 2
        for i in range(n-1):
            ss += reversed(ss)
            for j in range(halfLeng):
                ss[j] = '0' + ss[j]
            for j in range(halfLeng, 2*halfLeng):
                ss[j] = '1' + ss[j]
            halfLeng *= 2
        #halfLeng is now total length
        ss = [self.bits2decimal(i) for i in ss]
        return ss

sol = Solution()
print(sol.grayCode(0))


"""
0000
0001
0011
0010
0110
0111
0101
0100
1100
1101
1111
1110
1010
1011
1001
1000
"""