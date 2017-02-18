__author__ = 'Adward'
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        valid_ips = []
        cur_ip = []
        n = len(s)

        def valid_section(start, end):
            if start > end:
                return False
            if s[start] == '0' and start != end:
                return False
            if end - start > 1 and int(s[start:end + 1]) >= 256:
                return False
            return True

        def backTracking(start):
            if len(cur_ip) == 3:
                if valid_section(start, n - 1):
                    valid_ips.append('.'.join(cur_ip + [s[start:]]))
                return

            for end in range(start, min(n, start + 3)):
                if valid_section(start, end):
                    cur_ip.append(s[start:end + 1])
                    backTracking(end + 1)
                    cur_ip.pop()

        backTracking(0)
        return valid_ips

    def restoreIpAddresses0(self, s):
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