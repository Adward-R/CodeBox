class Solution(object):
    dict1 = ['One', 'Two', 'Three', 'Four', 'Five',
             'Six', 'Seven', 'Eight', 'Nine', 'Ten']
    dict2 = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
             'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    dict3 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
             'Seventy', 'Eighty', 'Ninety', 'Hundred']
    def ThreeDigitNumberToWords(self, num):
        res = ''
        #flag = False
        if num >= 100:
            #flag = True
            res = self.dict1[num//100-1] + ' Hundred '
        num %= 100
        if num == 0:
        	pass
        elif 1 <= num <= 10:
            #if flag:
            #    res += 'And '
            res += self.dict1[num-1] + ' '
        elif 10 < num < 20:
            res += self.dict2[num-11] + ' '
        else:
            res += self.dict3[num/10-2] + ' '
            num %= 10
            if num:
                res += self.dict1[num-1] + ' '
        return res

    def numberToWords(self, num):
    	if num == 0:
    		return 'Zero'
        res = ''
        if num >= 1000000000:
            res += self.dict1[num//1000000000-1] + ' Billion '
        num %= 1000000000
        if num >= 1000000:
            res += self.ThreeDigitNumberToWords(num//1000000) + 'Million '
        num %= 1000000
        if num >= 1000:
            res += self.ThreeDigitNumberToWords(num//1000) + 'Thousand '
        num %= 1000
        res += self.ThreeDigitNumberToWords(num)
        return res[0:-1]

sol = Solution()
print(sol.numberToWords(1001))

        
