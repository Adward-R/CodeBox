__author__ = 'Adward'
class WordDictionary(object):
    class TrieNode(object):
        def __init__(self):
            self.children = [None] * 26
            self.check = False

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = self.TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        p = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not p.children[idx]:
                p.children[idx] = self.TrieNode()
            p = p.children[idx]
        p.check = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def branchSearch(p, i, word):
            if i == len(word):
                return p.check
            w = word[i]
            if w == '.':
                for np in p.children:
                    if np and branchSearch(np, i+1, word):
                        return True
                return False
            else:
                idx = ord(w) - ord('a')
                if not p.children[idx]:
                    return False
                else:
                    return branchSearch(p.children[idx], i+1, word)

        return branchSearch(self.root, 0, word)


# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("b.."))