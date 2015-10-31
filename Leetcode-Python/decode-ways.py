__author__ = 'Adward'
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def numDecodings2(s):
            """
            :type s: str
            :rtype: int
            """
            if s == "":
                return 1
            q = [s]
            cnt = 0
            while len(q):
                ss = q[0]
                if len(ss) >= 2:
                    ns = int(ss[0:2])
                    if ns < 27:
                        q.append(ss[2:])
                    q.append(ss[1:])
                elif len(ss) == 0:
                    cnt += 1
                else:
                    ns = int(ss)
                    q.append("")
                q = q[1:]
            return cnt
        ###
        if s == "" or s[0] == "0":
            return 0
        cnt = 1
        ss = ""
        if s[0] == '1' or s[0] == '2':
            ss += s[0]
        i = 1
        while i < len(s):
            if 1 <= int(s[i]) <= 2:
                ss += s[i]
                i += 1
            else:
                if s[i] == '0':
                    if s[i-1] != '1' and s[i-1] != '2':
                        return 0
                    else:
                        ss = ss[0:-1]
                elif (3 <= int(s[i]) <= 6 and (s[i-1] == '1' or s[i-1] == '2'))\
                        or (7 <= int(s[i]) <= 9 and s[i-1] == '1'):# or s[i] == '0':
                    ss += s[i]

                cnt *= numDecodings2(ss)
                ss = ""
                i += 1
                while i < len(s) and s[i] != '1' and s[i] != '2':
                    if s[i] == '0' and s[i-1] != '1' and s[i-1] != '2':
                        return 0
                    i += 1
                if i < len(s):
                    if s[i] == '0' and s[i-1] != '1' and s[i-1] != '2':
                        return 0
                    ss += s[i]
                    i += 1
        cnt *= numDecodings2(ss)
        return cnt


sol = Solution()
print(sol.numDecodings("13121"))
print(sol.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"))
print(sol.numDecodings("101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010"))
print(sol.numDecodings("100"))