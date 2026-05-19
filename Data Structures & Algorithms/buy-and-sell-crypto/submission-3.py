class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = float('inf')
        profit = 0
        for price in prices:
            if lowest_price > price:
                lowest_price = price
            profit = max(profit, price-lowest_price)
        return profit