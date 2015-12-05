__author__ = 'Adward'
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        leng = len(num)
        if leng <= 2:
            return False
        idxLst = [0, 1, 2]
        #while num[idxLst[-1]] == '0':
        #    idxLst[-1] += 1

        while True:
            ssum = int(num[idxLst[-3]:idxLst[-2]]) + int(num[idxLst[-2]:idxLst[-1]])
            #print(ssum)
            sleng = len(str(ssum))
            if leng - idxLst[-1] == 0:
                return True
            #elif leng-idxLst[-1] < sleng:
            #    return False
            elif int(num[idxLst[-1]:idxLst[-1]+sleng]) == ssum:
                idxLst.append(idxLst[-1]+sleng)
            else:
                idxLst = idxLst[0:3]
                seg1 = '01'
                seg2 = '01'
                while str(int(seg1)) != seg1 or str(int(seg2)) != seg2:
                    idxLst[-1] += 1
                    if idxLst[-1] >= leng:
                        idxLst.pop()
                        idxLst[-1] += 1
                        idxLst.append(idxLst[-1]+1)
                        if idxLst[-1] >= leng:
                            return False
                    seg1 = num[idxLst[0]:idxLst[1]]
                    seg2 = num[idxLst[1]:idxLst[2]]

sol = Solution()
print(sol.isAdditiveNumber("12012122436"))