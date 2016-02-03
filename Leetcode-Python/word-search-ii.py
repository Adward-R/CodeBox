__author__ = 'Adward'
class Solution(object):
    class Trie(object):
        class TrieNode(object):
            def __init__(self):
                """
                Initialize your data structure here.
                """
                self.children = [None] * 26
                self.word = None

        def __init__(self):
            self.root = self.TrieNode()

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
                    p.children[idx] = self.TrieNode()
                p = p.children[idx]
            p.word = word

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def backTracing(pTrie, i, j):
            """
            :type pTrie: List[TrieNode]
            :type i: int
            :type j: int
            :rtype: Nothing
            """
            ch = self.board[i][j]
            if ch == '#':
                return
            else:
                npTrie = pTrie.children[ord(ch) - ord('a')]
                if not npTrie:
                    return
                else:
                    if npTrie.word:
                        self.selected.add(npTrie.word)
                    self.board[i][j] = '#'
                    if i < self.rowN - 1:
                        backTracing(npTrie, i+1, j)
                    if i > 0:
                        backTracing(npTrie, i-1, j)
                    if j < self.colN - 1:
                        backTracing(npTrie, i, j+1)
                    if j > 0:
                        backTracing(npTrie, i, j-1)
                    self.board[i][j] = ch

        self.trieTree = self.Trie()
        for word in words:
            self.trieTree.insert(word)

        if len(words) == 0:
            return []
        self.rowN = len(board)
        if self.rowN == 0:
            return []
        self.colN = len(board[0])
        if self.colN == 0:
            return []

        self.selected = set()
        self.board = board
        pTrie = self.trieTree.root
        for i in range(self.rowN):
            for j in range(self.colN):
                idx = ord(board[i][j]) - ord('a')
                if pTrie.children[idx] and backTracing(pTrie, i, j):
                    pass
        return list(self.selected)

sol = Solution()
'''
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain", "oei"]
'''
board = [
    ['a', 'b'],
    ['a', 'a']
]
words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
print(sol.findWords(board, words))