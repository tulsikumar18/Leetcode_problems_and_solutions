class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_profit = 0
        min_prices = float('inf')

        for i in range(len(prices)):

            if prices[i] < min_prices:
                min_prices = prices[i]
            else:
                profit = prices[i] - min_prices
                max_profit = max(max_profit, profit)

        return max_profit

