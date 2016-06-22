__author__ = 'Adward'


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1_idx, w2_idx = [], []
        for i in range(len(words)):
            if words[i] == word1:
                w1_idx.append(i)
            elif words[i] == word2:
                w2_idx.append(i)

        j = 0
        min_dist = len(words) - 1
        for i in range(len(w1_idx)):
            while j < len(w2_idx) and w2_idx[j] < w1_idx[i]:
                j += 1
            if j > 0:
                min_dist = min(min_dist, abs(w1_idx[i] - w2_idx[j-1]))
            if j < len(w2_idx):
                min_dist = min(min_dist, abs(w1_idx[i] - w2_idx[j]))

        return min_dist


sol = Solution()
words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
# word2 = "practice"
word2 = "makes"
print(sol.shortestDistance(words, word1, word2))


