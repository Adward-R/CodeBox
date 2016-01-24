__author__ = 'Adward'
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 1:
            if gas[0] - cost[0] >= 0:
                return 0
            else:
                return -1
        tank = gas[0] - cost[0]
        begin = 0
        p = 1
        while True:
            if p != begin:
                if tank >= 0:
                    tank += gas[p] - cost[p]
                else:
                    begin = p
                    if begin == 0: #pivot
                        break
                    tank = gas[begin] - cost[begin]
                p = (p+1) % len(gas)
            else:
                if tank >= 0:
                    return begin
                else:
                    return -1
        return -1

sol = Solution()
#gas = [6,2,2,3,5,6,2]
#cost = [2,10,1,3,2,6,6]
gas = [3,5]
cost = [4,5]
print(sol.canCompleteCircuit(gas, cost))