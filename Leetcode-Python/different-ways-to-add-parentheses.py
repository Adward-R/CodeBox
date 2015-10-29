__author__ = 'Adward'
class Solution(object):
    def divConquer(self, operands, operators):
        if len(operators) == 0:
            return operands
        elif len(operators) == 1:
            if operators[0] == '+':
                return [operands[0] + operands[1]]
            elif operators[0] == '-':
                return [operands[0] - operands[1]]
            else:
                return [operands[0] * operands[1]]
        else:
            lst = []
            for i in range(len(operators)):
                lst1 = self.divConquer(operands[0:i+1], operators[0:i])
                lst2 = self.divConquer(operands[i+1:], operators[i+1:])
                if operators[i] == '+':
                    for j in lst1:
                        for k in lst2:
                            lst.append(j+k)
                elif operators[i] == '-':
                    for j in lst1:
                        for k in lst2:
                            lst.append(j-k)
                else: # '*'
                    for j in lst1:
                        for k in lst2:
                            lst.append(j*k)
            return lst

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        idxs = []
        operands = []
        operators = []
        for i in range(len(input)):
            if not input[i].isdigit():
                idxs.append(i)
        if len(idxs) == 0:
            return [int(input)]

        for idx in idxs:
            operators.append(input[idx])
        operands.append(int(input[0:idxs[0]]))
        for i in range(len(idxs)-1):
            operands.append(int(input[idxs[i]+1:idxs[i+1]]))
        operands.append(int(input[idxs[-1]+1:]))

        return self.divConquer(operands, operators)

sol = Solution()
print(sol.diffWaysToCompute("-5"))