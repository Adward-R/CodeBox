__author__ = 'Adward'
class Solution(object):
    def coinChange4(self, coins, amount):  # DP
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp[i] stands for coinChange(coins, i)
        dp = [0] + [amount + 1] * amount  # fill with MAX
        coins.sort()
        for i in range(1, amount+1):
            for c in coins:
                if c > i:  # pruning
                    break
                dp[i] = min(dp[i], dp[i - c] + 1)
        return -1 if dp[amount] > amount else dp[amount]


    def coinChange3(self, coins, amount):  # TLE backtracking
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        self.minCoinNum = amount + 1

        def backTracking(dist, tmpCoin, i):
            if i + 1 == len(coins):
                if dist % coins[i] == 0:
                    self.minCoinNum = min(self.minCoinNum, tmpCoin + dist // coins[i])
            elif tmpCoin < self.minCoinNum:  # else pruned
                for j in range(dist//coins[i]+1):
                    backTracking(dist - j * coins[i], tmpCoin + j, i + 1)

        backTracking(amount, 0, 0)
        return -1 if self.minCoinNum == amount + 1 else self.minCoinNum


    def coinChange2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        if amount == 0:
            return 0
        elif amount < coins[0]:
            return -1
        elif amount <= coins[-1]:
            if amount in coins:
                return 1
            else:
                while coins[-1] > amount:
                    coins.pop()
        #coinTypeNum = len(coins)
        maxCoinNum = int(amount / coins[0]) + 1
        ladder = [None] * (amount+1)
        invIdx = []
        for i in range(maxCoinNum+1):
            invIdx.append([])
        for c in coins:
            ladder[c] = 1
            invIdx[1].append(c)
        if ladder[-1]:
            return ladder[-1]

        for coinNum in range(2, maxCoinNum+1):
            part1 = 1
            part2 = coinNum - 1
            while part1 <= part2:
                for i in invIdx[part1]:
                    for j in invIdx[part2]:
                        if i+j <= amount and not ladder[i+j]:
                            ladder[i+j] = coinNum
                            invIdx[coinNum].append(i+j)
                            if ladder[-1]:
                                for i in range(amount+1):
                                    print(str(i)+'|'+str(ladder[i]))
                                return ladder[-1]
                part1 += 1
                part2 -= 1
        return -1

    def coinChange1(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        def coinChangeRec(coins, amount, ladder):
            if ladder[amount]:
                return ladder[amount]
            else:
                minRes = int(amount / coins[0]) + 1
                part1 = coins[0]
                part2 = amount-coins[0]
                while part1 <= part2:
                    tmp = coinChangeRec(coins, part1, ladder) + \
                         coinChangeRec(coins, part2, ladder)
                    if tmp < minRes:
                        minRes = tmp
                    part1 += coins[0]
                    part2 -= coins[0]
                ladder[amount] = minRes
                return minRes

        coins.sort()
        ladder = [None] * (amount+1)
        for c in coins:
            ladder[c] = 1
        res = coinChangeRec(coins, amount, ladder)
        for i in range(amount+1):
            print(str(i)+'|'+str(ladder[i]))
        return res

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount <= 0:
            return 0
        coins.sort(reverse=True)
        ladder = [0] * len(coins)
        ssum = 0
        i = 0
        coinN = 0
        MAX_INT = 2**31 - 1
        minCoinN = MAX_INT
        while ssum <= amount:
            ladder[i] = (amount - ssum) // coins[i]
            ssum += ladder[i] * coins[i]
            coinN += ladder[i]
            if ssum == amount:
                #print(sum(ladder), ladder)
                minCoinN = min(minCoinN, coinN)
                #return sum(ladder)
            i += 1
            while coinN > minCoinN or i >= len(coins):
                i -= 1
                while i >= 0 and ladder[i] <= 0:
                    i -= 1
                if i >= 0:
                    ladder[i] -= 1
                    ssum -= coins[i]
                    coinN -= 1
                    i += 1
                else:
                    if minCoinN < MAX_INT:
                        return minCoinN
                    else:
                        return -1

        if minCoinN:
            return minCoinN
        else:
            return -1


sol = Solution()
'''
print(sol.coinChange([1], 0))
print(sol.coinChange([1,2,5],11))
print(sol.coinChange([357,239,73,52], 9832))
print(sol.coinChange([53,5,2,1], 900))
print(sol.coinChange([186,419,83,408], 6249))

print(sol.coinChange([436,405,7,3], 8839)) #25
'''
print(sol.coinChange3([216,94,15,86], 5372))
print(sol.coinChange4([288,160,10,249,40,77,314,429], 9208))