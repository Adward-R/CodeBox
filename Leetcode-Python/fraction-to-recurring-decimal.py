__author__ = 'Adward'
class Solution(object):
    def gcd(self, numerator, denominator):
        rev = False
        if denominator > numerator:
            rev = True
        while numerator and denominator:
            if rev:
                denominator %= numerator
            else:
                numerator %= denominator
            rev = not rev
        if numerator:
            return numerator
        else:
            return denominator

    def timesOf2and5(self, num):
        while num % 2 == 0:
            num /= 2
        while num % 5 == 0:
            num /= 5
        if num == 1:
            return True
        else:
            return False

    def decimalGen(self, n, d, leng):
        s = ''
        while n >= d:
            n -= d
        for i in range(leng):
            n *= 10
            quotient = int(n/d)
            s += str(quotient)
            n -= quotient * d
        return s

    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'
        flag = 1
        if numerator < 0:
            numerator = -numerator
            flag = -flag
        if denominator < 0:
            denominator = -denominator
            flag = -flag

        maxCommonDeno = self.gcd(numerator, denominator)
        if maxCommonDeno != 1:
            numerator /= maxCommonDeno
            denominator /= maxCommonDeno
        if denominator == 1:
            ss = str(int(numerator))
            if flag == -1:
                ss = '-' + ss
            return ss
        elif self.timesOf2and5(denominator):
        	intPart = int(numerator/denominator)
        	numerator -= intPart * denominator
        	ss = self.decimalGen(numerator, denominator, 31)
        	lastZero = 30
        	while ss[lastZero] == '0':
        		lastZero -= 1
        	ss = str(intPart) + '.' + ss[0:lastZero+1]
        	if flag == -1:
        		ss = '-' + ss
        	return ss
        else:
            n = numerator/denominator
            #quick pass begin
            if numerator > 2147483647:
            	intPart = int(n)
            	numerator -= intPart * denominator
            	ss = str(intPart)+ '.(' + self.decimalGen(numerator, denominator, 999) + ')'
            	if flag == -1:
            		ss = '-' + ss
            	return ss
            #quick pass end

            intPart = int(n)
            numerator -= intPart * denominator
            sLeng = 0
            while True:
            	sLeng += 100
                s = self.decimalGen(numerator, denominator, sLeng)
                #print(s)
                cBegin = 0
                cLeng = 1
                while cBegin < sLeng - 10: #len(s)
                	#special case for cLeng==1
                    repeat = s[cBegin]
                    repeatFlag = True
                    for j in range(1, 11):
                    	if s[cBegin+j] != repeat:
                    		repeatFlag = False
                    		break
                    if repeatFlag:
                        ss = str(intPart) + '.' + s[0:cBegin] + '(' + s[cBegin] +')'
                        if flag == -1:
                            ss = '-' + ss
                        return ss

                    #special case for cLeng==2
                    repeat = s[cBegin:cBegin+2]
#                    print(s)	
                    repeatFlag = True
                    for j in range(1, 10):
                    	if s[cBegin+2*j:cBegin+2*j+2] != repeat:
                    		repeatFlag = False
                    		break
                    if repeatFlag:
                        ss = str(intPart) + '.' + s[0:cBegin] + '(' + s[cBegin:cBegin+2] +')'
                        if flag == -1:
                            ss = '-' + ss
                        return ss
                    
                    cLeng = 3
                    while cLeng < len(s)-cBegin:
                        if s[cBegin:cBegin+cLeng] == s[cBegin+cLeng:cBegin+2*cLeng] \
                                == s[cBegin+2*cLeng:cBegin+3*cLeng]:
                            ss = str(intPart) + '.' + s[0:cBegin] + '(' + s[cBegin:cBegin+cLeng] +')'
                            if flag == -1:
                                ss = '-' + ss
                            return ss
                        else:
                            cLeng += 1


                    cLeng = 1
                    cBegin += 1


sol = Solution()
#for i in range(1, 100):
#    print(sol.fractionToDecimal(1,i))
print(sol.fractionToDecimal(-2147483648, -10)) #"0.0000000004656612873077392578125"
print(sol.fractionToDecimal(-1,-2147483648)) #"0.0000000004656612873077392578125"
print(sol.fractionToDecimal(1, 99)) #0.(01)
print(sol.fractionToDecimal(500, 10))
print(sol.fractionToDecimal(1, 19)) #"0.(052631578947368421)"
print(sol.fractionToDecimal(1, 214748364)) #"0.00(000000465661289042462740251655654056577585848337359161441621040707904997124914069194026549138227660723878669455195477065427143370461252966751355553982241280310754777158628319049732085502639731402098131932683780538602845887105337854867197032523144157689601770377165713821223802198558308923834223016478952081795603341592860749337303449725)"
print(sol.fractionToDecimal(-2147483648, -1999))
#print(2147483647/37) 