__author__ = 'Adward'
from collections import defaultdict, deque
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        pred = defaultdict(set)
        succ = defaultdict(set)
        for i in range(len(words)-1):
            length = min(len(words[i]), len(words[i+1]))
            for j in range(length):
                if words[i][j] != words[i+1][j]:
                    succ[words[i][j]].add(words[i+1][j])
                    pred[words[i+1][j]].add(words[i][j])
                    break
            else:
                if len(words[i]) > len(words[i+1]):
                    return ''

        alphabet = set(''.join(words))
        # alphabet = set(pred)
        # alphabet.update(set(succ))
        indegree = {key: len(pred[key]) for key in alphabet}
        unassigned = deque(filter(lambda ch: indegree[ch] == 0, indegree))

        alien_order = []
        while len(unassigned):
            v = unassigned.popleft()
            alien_order.append(v)
            for w in succ[v]:
                indegree[w] -= 1
                if indegree[w] == 0:
                    unassigned.append(w)
        if len(alien_order) != len(alphabet):
            return ''
        else:
            return ''.join(alien_order)

sol = Solution()
# words = ["wrt","wrf","er","ett","rftt"]
words = ["za", "zb", "ca", "cb"]
print(sol.alienOrder(words))




