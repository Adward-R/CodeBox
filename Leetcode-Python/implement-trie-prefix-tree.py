__author__ = 'Adward'
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None] * 26
        self.check = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not p.children[idx]:
                p.children[idx] = TrieNode()
            p = p.children[idx]
        p.check = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not p.children[idx]:
                return False
            else:
                p = p.children[idx]
        return p.check

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not p.children[idx]:
                return False
            else:
                p = p.children[idx]
        return True

trie = Trie()
trie.insert('abc')
trie.insert('abde')
print(trie.search("abde"))
print(trie.startsWith('ab'))