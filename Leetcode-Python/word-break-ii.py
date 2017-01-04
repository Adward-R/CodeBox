__author__ = 'Adward'
from time import time
class Solution(object):
    class Trie(object):
        class TrieNode(object):
            def __init__(self):
                self.children = [None] * 26
                self.check = False

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
            p.check = True

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        def wBreak(s, i):
            _i = i
            if self.tmpResults[i] is False:
                return False

            #print(i)
            p = self.trie.root
            probableIs = []
            self.seq.append(i)

            while i < len(s):
                if p.check:
                    probableIs.append(i)
                idx = ord(s[i]) - ord('a')
                if not p.children[idx]:
                    break
                else:
                    p = p.children[idx]
                i += 1

            flag = True
            for j in range(len(probableIs)-1, -1, -1):
                ii = probableIs[j]
                wBreak(s, ii)
                if self.tmpResults[ii] is None:
                    flag = False

            if i == len(s):
                if p.check:
                    self.seq.append(len(s))
                    self.wbreaks.append(" ".join([s[self.seq[k]:self.seq[k+1]] for k in range(len(self.seq)-1)]))
                    self.seq.pop()
                elif flag:
                    self.tmpResults[i-1] = False
            #elif i == _i:
            #r    self.tmpResults[_i] = False
            elif flag or len(probableIs) == 0:
                self.tmpResults[_i] = False
            self.seq.pop()

        self.trie = self.Trie()
        for word in wordDict:
            self.trie.insert(word)
        self.tmpResults = [None] * len(s) + [None]
        self.wbreaks = []
        self.seq = []
        wBreak(s, 0)
        return self.wbreaks

class Solution1(object):
    def __init__(self):
        self.cache = {}  # str -> List[str]

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        if s in self.cache:  # take from memory
            return self.cache[s]
        ans = []
        if s in wordDict:  # the whole str in a word
            ans.append(s)

        for i in range(1, len(s)):
            word = s[i:]
            if word in wordDict:
                prev = self.wordBreak(s[:i], wordDict)
                prev = [seg + ' ' + word for  seg in prev]
                ans += prev
        self.cache[s] = ans
        return ans


sol = Solution1()
t = time()

# s = 'lecooco'
# wordDict = ['le', 'co', 'coo']
# print(sol.wordBreak(s, wordDict))
#
# s = 'a'*150+'b'
# wordDict = ['a'*(i+1) for i in range(10)]
# print(sol.wordBreak(s, wordDict))
#
# s = 'a'*75+'baab'+'b'*72
# wordDict = ['a'*(i+2) for i in range(9)] + ['ba']
# print(sol.wordBreak(s, wordDict))
#
# s = "fohhemkkaecojceoaejkkoedkofhmohkcjmkggcmnami"
# wordDict = ["kfomka","hecagbngambii","anobmnikj","c","nnkmfelneemfgcl","ah","bgomgohl","lcbjbg","ebjfoiddndih","hjknoamjbfhckb","eioldlijmmla","nbekmcnakif","fgahmihodolmhbi","gnjfe","hk","b","jbfgm","ecojceoaejkkoed","cemodhmbcmgl","j","gdcnjj","kolaijoicbc","liibjjcini","lmbenj","eklingemgdjncaa","m","hkh","fblb","fk","nnfkfanaga","eldjml","iejn","gbmjfdooeeko","jafogijka","ngnfggojmhclkjd","bfagnfclg","imkeobcdidiifbm","ogeo","gicjog","cjnibenelm","ogoloc","edciifkaff","kbeeg","nebn","jdd","aeojhclmdn","dilbhl","dkk","bgmck","ohgkefkadonafg","labem","fheoglj","gkcanacfjfhogjc","eglkcddd","lelelihakeh","hhjijfiodfi","enehbibnhfjd","gkm","ggj","ag","hhhjogk","lllicdhihn","goakjjnk","lhbn","fhheedadamlnedh","bin","cl","ggjljjjf","fdcdaobhlhgj","nijlf","i","gaemagobjfc","dg","g","jhlelodgeekj","hcimohlni","fdoiohikhacgb","k","doiaigclm","bdfaoncbhfkdbjd","f","jaikbciac","cjgadmfoodmba","molokllh","gfkngeebnggo","lahd","n","ehfngoc","lejfcee","kofhmoh","cgda","de","kljnicikjeh","edomdbibhif","jehdkgmmofihdi","hifcjkloebel","gcghgbemjege","kobhhefbbb","aaikgaolhllhlm","akg","kmmikgkhnn","dnamfhaf","mjhj","ifadcgmgjaa","acnjehgkflgkd","bjj","maihjn","ojakklhl","ign","jhd","kndkhbebgh","amljjfeahcdlfdg","fnboolobch","gcclgcoaojc","kfokbbkllmcd","fec","dljma","noa","cfjie","fohhemkka","bfaldajf","nbk","kmbnjoalnhki","ccieabbnlhbjmj","nmacelialookal","hdlefnbmgklo","bfbblofk","doohocnadd","klmed","e","hkkcmbljlojkghm","jjiadlgf","ogadjhambjikce","bglghjndlk","gackokkbhj","oofohdogb","leiolllnjj","edekdnibja","gjhglilocif","ccfnfjalchc","gl","ihee","cfgccdmecem","mdmcdgjelhgk","laboglchdhbk","ajmiim","cebhalkngloae","hgohednmkahdi","ddiecjnkmgbbei","ajaengmcdlbk","kgg","ndchkjdn","heklaamafiomea","ehg","imelcifnhkae","hcgadilb","elndjcodnhcc","nkjd","gjnfkogkjeobo","eolega","lm","jddfkfbbbhia","cddmfeckheeo","bfnmaalmjdb","fbcg","ko","mojfj","kk","bbljjnnikdhg","l","calbc","mkekn","ejlhdk","hkebdiebecf","emhelbbda","mlba","ckjmih","odfacclfl","lgfjjbgookmnoe","begnkogf","gakojeblk","bfflcmdko","cfdclljcg","ho","fo","acmi","oemknmffgcio","mlkhk","kfhkndmdojhidg","ckfcibmnikn","dgoecamdliaeeoa","ocealkbbec","kbmmihb","ncikad","hi","nccjbnldneijc","hgiccigeehmdl","dlfmjhmioa","kmff","gfhkd","okiamg","ekdbamm","fc","neg","cfmo","ccgahikbbl","khhoc","elbg","cbghbacjbfm","jkagbmfgemjfg","ijceidhhajmja","imibemhdg","ja","idkfd","ndogdkjjkf","fhic","ooajkki","fdnjhh","ba","jdlnidngkfffbmi","jddjfnnjoidcnm","kghljjikbacd","idllbbn","d","mgkajbnjedeiee","fbllleanknmoomb","lom","kofjmmjm","mcdlbglonin","gcnboanh","fggii","fdkbmic","bbiln","cdjcjhonjgiagkb","kooenbeoongcle","cecnlfbaanckdkj","fejlmog","fanekdneoaammb","maojbcegdamn","bcmanmjdeabdo","amloj","adgoej","jh","fhf","cogdljlgek","o","joeiajlioggj","oncal","lbgg","elainnbffk","hbdi","femcanllndoh","ke","hmib","nagfahhljh","ibifdlfeechcbal","knec","oegfcghlgalcnno","abiefmjldmln","mlfglgni","jkofhjeb","ifjbneblfldjel","nahhcimkjhjgb","cdgkbn","nnklfbeecgedie","gmllmjbodhgllc","hogollongjo","fmoinacebll","fkngbganmh","jgdblmhlmfij","fkkdjknahamcfb","aieakdokibj","hddlcdiailhd","iajhmg","jenocgo","embdib","dghbmljjogka","bahcggjgmlf","fb","jldkcfom","mfi","kdkke","odhbl","jin","kcjmkggcmnami","kofig","bid","ohnohi","fcbojdgoaoa","dj","ifkbmbod","dhdedohlghk","nmkeakohicfdjf","ahbifnnoaldgbj","egldeibiinoac","iehfhjjjmil","bmeimi","ombngooicknel","lfdkngobmik","ifjcjkfnmgjcnmi","fmf","aoeaa","an","ffgddcjblehhggo","hijfdcchdilcl","hacbaamkhblnkk","najefebghcbkjfl","hcnnlogjfmmjcma","njgcogemlnohl","ihejh","ej","ofn","ggcklj","omah","hg","obk","giig","cklna","lihaiollfnem","ionlnlhjckf","cfdlijnmgjoebl","dloehimen","acggkacahfhkdne","iecd","gn","odgbnalk","ahfhcd","dghlag","bchfe","dldblmnbifnmlo","cffhbijal","dbddifnojfibha","mhh","cjjol","fed","bhcnf","ciiibbedklnnk","ikniooicmm","ejf","ammeennkcdgbjco","jmhmd","cek","bjbhcmda","kfjmhbf","chjmmnea","ifccifn","naedmco","iohchafbega","kjejfhbco","anlhhhhg"]
# print(sol.wordBreak(s, wordDict))

s = "aaaaaaa"
wordDict = ["aaaa", "aa", "a"]
res = sol.wordBreak(s, wordDict)
print(len(res), res)

# s = "aaaaaaa"
# wordDict = ["aaaa", "aa"]
# print(sol.wordBreak(s, wordDict))
#
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# print(sol.wordBreak(s, wordDict))
#
# s = 'a'*150+'b'
# wordDict = ["a","aa","ba"]
# print(sol.wordBreak(s, wordDict))

print(time()-t)