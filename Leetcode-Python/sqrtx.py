__author__ = 'Adward'
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -1
        elif x == 0:
            return 0
        elif 1 <= x < 4:
            return 1

        bbase = 2
        ppow = 4
        powMul = 16
        while powMul < x:
            ppow = powMul
            bbase *= bbase
            powMul *= powMul
        lleft = bbase
        rright = bbase * bbase
        while lleft + 1 < rright:
            mmid = (lleft + rright) // 2
            _x = mmid * mmid
            if _x > x:
                rright = mmid
            elif _x < x:
                lleft = mmid
            else:
                return mmid
        if lleft * lleft <= x < rright * rright:
            return lleft
        else:
            return rright

        # 4 16 256 65536
        # 2 4  16  256
        # 1 2  4   8
        # 0 1  2   3

sol = Solution()
print(sol.mySqrt(3))