__author__ = 'Adward'


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        spaces = [-1]
        for i in range(len(s)):
            if s[i] == ' ':
                spaces.append(i)
        spaces.append(len(s))

        # print(spaces)
        # print(s)

        for k in range(len(spaces)-1):
            i, j = spaces[k] + 1, spaces[k+1] - 1
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1


sol = Solution()
s = list('abc bbc eft k')
# s = list('a b')
sol.reverseWords(s)
print(s)