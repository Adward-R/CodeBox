__author__ = 'Adward'
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words.sort(key=len)
        shorterWords = {words[0]}
        ans = []
        for word in words[1:]:
            dp = [True] + [False] * len(word)
            for i in range(1, len(word)+1):
                for j in range(i):
                    if not dp[j]:
                        continue
                    if dp[j] and word[j:i] in shorterWords:
                        dp[i] = True
                        break
            if dp[-1]:
                ans.append(word)
            shorterWords.add(word)
        return ans

sol = Solution()
words = ["cat","dog","catdog"]
print(sol.findAllConcatenatedWordsInADict(words))