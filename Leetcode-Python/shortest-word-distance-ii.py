__author__ = 'Adward'


class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.leng_words = len(words)
        self.indexes = {}
        for i in range(len(words)):
            if words[i] in self.indexes:
                self.indexes[words[i]].append(i)
            else:
                self.indexes[words[i]] = [i]

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1_idx, w2_idx = self.indexes[word1], self.indexes[word2]
        j = 0
        min_dist = self.leng_words - 1
        for i in range(len(w1_idx)):
            while j < len(w2_idx) and w2_idx[j] < w1_idx[i]:
                j += 1
            if j > 0:
                min_dist = min(min_dist, abs(w1_idx[i] - w2_idx[j-1]))
            if j < len(w2_idx):
                min_dist = min(min_dist, abs(w1_idx[i] - w2_idx[j]))

        return min_dist

# Your WordDistance object will be instantiated and called as such:
words = ["practice", "makes", "perfect", "coding", "makes"]
wordDistance = WordDistance(words)
print(wordDistance.shortest("coding", "practice"))
print(wordDistance.shortest("makes", "coding"))