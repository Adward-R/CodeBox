__author__ = 'Adward'
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = []
        for i in range(len(s)):
            ch = s[i]
            if ch != ']':
                stk.append(ch)
            else:
                j = len(stk) - 1
                while j >= 0 and stk[j] != '[':
                    j -= 1
                k = j - 1  # j->'['
                while k >= 0 and stk[k].isdigit():
                    k -= 1
                num = int(''.join(stk[k+1:j]))
                stk = stk[:k+1] + num * stk[j+1:]
        return ''.join(stk)


sol = Solution()
ss = [
    "2[2[abc]3[cd]ef]",
    "3[a2[c]]",
    "2[abc]3[cd]ef",
    "2[a2[b2[c]]]"
]
for s in ss:
    print(sol.decodeString(s))