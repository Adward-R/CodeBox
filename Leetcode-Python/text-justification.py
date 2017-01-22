__author__ = 'Adward'
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if len(words) == 0:
            return []
        ans = []
        i, j = 0, 1
        curWidth = len(words[0])
        while True:
            while j < len(words) and curWidth + len(words[j]) + j - i <= maxWidth:
                curWidth += len(words[j])  # (j-i) -> minimum spaces needed between words in a line
                j += 1
            # fit words[i:j] into this line
            if j == len(words):
                ans.append(' '.join(words[i:j]).ljust(maxWidth))
                break

            line = words[i]
            if j-i == 1:
                line = line.ljust(maxWidth)
            else:
                totalSpaces = maxWidth - curWidth
                evenSpaces = totalSpaces // (j-i-1)
                n_larger = totalSpaces - evenSpaces * (j-i-1)
                for k in range(i+1, j):
                    line += ' ' * (evenSpaces+1 if k <= i+n_larger else evenSpaces) + words[k]
            ans.append(line)
            i, j = j, j + 1
            curWidth = len(words[i])
        return ans

'''
Distribute spaces in each line as evenly as possible:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]
'''