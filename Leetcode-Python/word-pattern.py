__author__ = 'Adward'
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(' ')
        dict = {}
        idx = 0
        try:
            for letter in pattern:
                if letter not in dict.keys():
                    if words[idx] not in dict.values():
                        dict[letter] = words[idx]
                    else:
                        return False
                else:
                    if dict[letter] != words[idx]:
                        return False
                idx += 1
        except:
            return False
        if idx != len(words):
            return False
        return True

sol = Solution()
print(sol.wordPattern('aaa', "dog dog dog dog"))