__author__ = 'Adward'
class Solution(object):
    def maxProfit(self, prices):
        """
        :param prices: List[int]
        :return: int
        """
        # before day i, what is the maxProfit for any seq end with buy/sell:
        #   buy[i] = max(sell[i-2]-price[i], buy[i-1])
        #   sell[i] = max(buy[i-1]+price[i], sell[i-1])
        if len(prices) < 2:
            return 0
        prev_buy, cur_buy = 0, -prices[0]  # max(0, prices[1]-prices[0])
        prev_sell, cur_sell = 0, 0
        for price in prices:
            prev_buy = cur_buy
            cur_buy = max(prev_sell - price, prev_buy)
            prev_sell = cur_sell
            cur_sell = max(prev_buy + price, prev_sell)
        return cur_sell

sol = Solution()
prices = [1,2,3,0,2]
print(sol.maxProfit(prices))