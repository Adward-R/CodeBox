__author__ = 'Adward'
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = []
        for tok in tokens:
            try:
                num = int(tok)
                stk.append(num)
            except:
                dnum = stk[-1]
                stk.pop()
                if tok == '+':
                    dnum += stk[-1]
                elif tok == '-':
                    dnum  = stk[-1] - dnum
                elif tok == '*':
                    dnum *= stk[-1]
                else:
                    if stk[-1] == 0:
                        dnum = 0
                    elif stk[-1] * dnum > 0:
                        dnum = int(abs(stk[-1]) / abs(dnum))
                    else:
                        dnum = - int(abs(stk[-1]) / abs(dnum))
                stk.pop()
                stk.append(dnum)
        return stk[0]

sol = Solution()
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
#print(sol.evalRPN(["4", "13", "5", "/", "+"]))
#print(sol.evalRPN(["2", "1", "+", "3", "*"]))
