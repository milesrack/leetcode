class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest = max(prices)
        profit = 0
        for price in prices:
            lowest = min(lowest, price)
            profit = max(profit, price-lowest)
        return profit
        