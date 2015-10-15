__author__ = 'Adward'
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        leng = len(s)
        if leng > 12 or leng < 4:
            return []
        heads = []

        for h1 in range(1, 4):
            for h2 in range(h1+1, h1+4):
                for h3 in range(h2+1, h2+4):
                    if 1 <= leng - h3 <= 3:
                        heads.append([h1, h2, h3])

        ips = []
        for h in heads:
            s1, s2, s3, s4 = s[0:h[0]], s[h[0]:h[1]], s[h[1]:h[2]], s[h[2]:]
            if (s1[0] == '0' and len(s1) > 1) or (s2[0] == '0' and len(s2) > 1)\
                    or (s3[0] == '0' and len(s3) > 1) or (s4[0] == '0' and len(s4) > 1):
                continue
            if int(s1) > 255 or int(s2) > 255 \
                    or int(s3) > 255 or int(s4) > 255:
                continue
            ips.append(s1 + '.' + s2 + '.' + s3 + '.' + s4)
        return ips

sol = Solution()
print(sol.restoreIpAddresses('010010'))