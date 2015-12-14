__author__ = 'Adward'
class Solution(object):
    def convert0(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        N = len(s)
        if numRows <= 1:
            return s
        elif numRows == 2:
            ss = ''
            if N % 2 == 0:
                for i in range(0, N, 2):
                    ss += s[i]
                for i in range(1, N, 2):
                    ss += s[i]
            return ss

        zigzag = []
        numCols = (numRows-1) * (int(N/(numRows*2-2)) + 2)
        for i in range(numRows):
            zigzag.append([None] * numCols)
        rn = 0
        cn = 0
        mode = True # downwards
        for ch in s:
            if mode:
                if rn >= numRows:
                    mode = False
                    zigzag[rn-2][cn+1] = ch
                    rn -= 3
                    cn += 2
                else:
                    zigzag[rn][cn] = ch
                    rn += 1
            else:
                zigzag[rn][cn] = ch
                if rn <= 0:
                    mode = True
                    rn = 1
                else:
                    rn -= 1
                    cn += 1

        ss = ''
        for i in range(numRows):
            #line = ''
            for j in range(numCols):
                if zigzag[i][j]:
                    ss += zigzag[i][j]
                #    line += zigzag[i][j]
                #else:
                #    line += ' '
            #print(line)
        return ss

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        N = len(s)
        if numRows <= 1:
            return s
        '''
        elif numRows == 2:
            ss = ''
            if N % 2 == 0:
                for i in range(0, N, 2):
                    ss += s[i]
                for i in range(1, N, 2):
                    ss += s[i]
            return ss
        '''
        ss = ''
        steps = [numRows * 2 - 2, 0]
        for i in range(numRows):
            j = i
            if steps[0] == 0:
                while j < N:
                    ss += s[j]
                    j += steps[1]
            elif steps[1] == 0:
                while j < N:
                    ss += s[j]
                    j += steps[0]
            else:
                turn = 0
                while j < N:
                    ss += s[j]
                    j += steps[turn]
                    turn = 1 - turn

            steps[0] -= 2
            steps[1] += 2

        return ss

sol = Solution()
print(sol.convert('AB', 2))
#print(sol.convert0('PAYPALISHIRING', 2))
#print(sol.convert('PALL', 1))
#print(sol.convert("maptvhyyewsggiuasuakgzumqwotffqrhglcpldthvzpdwpvqpizqclgabbfgrznxmrnzuigpkxvgosyfaxxeidflgmrzngzzymyswgkgdfotxnyakvevalgiyailghngvnbtulazsqvpftrqrwnrhtahvkvcrkkoxlhtyjvsaqifjbxaxkuhgwqbglfzvqnvduoeejwgzgnlinnhzhofffhlsokqgxlkuzqalmimvxxdknkkwbrcganapaqvzbhtdxvomdahdamnnwzjzrlhtbiidygccnyfntvbzviexurkstwsmjzfkjqniwsmlqralmbmjlqjfkvadrurbvwnfobpmvbyluawicltnbcvnyxsprjsmigtwjijeljrflpnnahdelarjxkbqttebbyakijquuhbfxrvxyabjavvzfwrarvctvedenwajdboaulasldenybmfxdgobkjwopcdlcmogcraotvzybnxcbebfkrgubeiqhldlzttckwqfrpeuedwghxnsovorzzhimkumepoqlgwevcycfwiovxgksxdtwlcixyudnkuzqsdoweqbaapyxykrxnktymdykabykxzbrernkhqnjiliivzfijyjwdhidkiokhrboipyrhlapwixrhccscloguzjehzorqsfahdrortgnddhkijfkuvsoucucblvudaumfm",549))