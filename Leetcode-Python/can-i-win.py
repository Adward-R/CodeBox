class Solution(object):

    def canIWin(self, maxChoosableInteger, desiredTotal):  # beats 82% without self.remain
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        pool = ['0'] + ['1'] * maxChoosableInteger
        # self.remain = maxChoosableInteger
        maps = {}
        if (1 + maxChoosableInteger) * maxChoosableInteger < desiredTotal * 2:
            return False

        def canWin(curTotal):
            status = ''.join(pool)
            if status in maps:
                return maps[status]
            # elif desiredTotal != curTotal and self.remain == 0:
            #     maps[status] = False
            #     return False

            for num in range(desiredTotal - curTotal, maxChoosableInteger + 1):
                if pool[num] == '1':
                    maps[status] = True
                    return True

            for num in range(min(desiredTotal - curTotal - 1, maxChoosableInteger), 0, -1):
                if pool[num] == '0':
                    continue
                pool[num] = '0'
                # self.remain -= 1
                if not canWin(curTotal + num):  # opponent's turn
                    # self.remain += 1
                    pool[num] = '1'
                    maps[status] = True
                    return True
                # self.remain += 1
                pool[num] = '1'

            maps[status] = False
            return False

        return canWin(0)

sol = Solution()
print(sol.canIWin(10, 40))  # F
print(sol.canIWin(10, 11))  # F
print(sol.canIWin(4, 6))  # T
print(sol.canIWin(20, 210))