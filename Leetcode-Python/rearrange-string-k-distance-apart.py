__author__ = 'Adward'
from collections import defaultdict
class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        cnt = defaultdict(int)
        valid = defaultdict(int)
        for ch in str:
            cnt[ch] += 1

        ans = []
        for i in range(len(str)):
            candidates = filter(lambda x: i >= valid[x], cnt)
            try:
                c = max(candidates, key=lambda x: cnt[x])
            except ValueError:
                return ""
            cnt[c] -= 1
            if cnt[c] == 0:
                del cnt[c]
            valid[c] = i + k
            ans.append(c)

        return ''.join(ans)
        # N = 26
        # cnt = [0] * N
        # valid = [0] * N
        # for ch in str:
        #     cnt[ord(ch)-ord('a')] += 1
        #
        # def findMaxValid(pos):
        #     candidates = filter(lambda x: cnt[x] > 0 and pos >= valid[x], range(N))
        #     try:
        #         return max(candidates, key=lambda x: cnt[x])
        #     except ValueError:
        #         return -1
        #
        # ans = []
        # for i in range(len(str)):
        #     ind = findMaxValid(i)
        #     if ind == -1:
        #         return ""
        #     cnt[ind] -= 1
        #     valid[ind] = i + k
        #     ans.append(chr(ord('a')+ind))
        #
        # return ''.join(ans)

    def rearrangeString0(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        if k <= 1:
            return str
        letterCnt = defaultdict(int)
        for ch in str:
            letterCnt[ch] += 1
        maxRep = max(letterCnt.values())
        rep = [[] for _ in range(maxRep+1)]
        for ch in letterCnt:
            rep[letterCnt[ch]].append(ch)
        frozeCounter = {}
        defrozed = []
        ans = []
        while True:
            for ch in frozeCounter:
                if frozeCounter[ch]:
                    frozeCounter[ch] -= 1
                    if frozeCounter[ch] == 0:
                        defrozed.append(ch)

            while len(rep) and len(rep[-1]) == 0:
                rep.pop()
            if len(defrozed) and defrozed[-1]:
                ch = defrozed.pop()
            else:

                if len(rep) == 0:
                    break
                ch = rep[-1].pop()
            ans.append(ch)
            letterCnt[ch] -= 1
            if letterCnt[ch]:  # still not exhausted
                frozeCounter[ch] = k
        if len(ans) == len(str):
            return ''.join(ans)
        else:
            return ""

sol = Solution()
print(sol.rearrangeString("aaabc", 3))