class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # start on opposite sides to get good profit prices and initialize max_profit to 0
        max_profit = 0
        L, R = 0, 1 
        while R < len(prices):
            # if L is equal or bigger than R, that means no profit, so increment L, otherwise decrement R
            # when something would have profit
            if prices[R] > prices[L]:
                # calculate max_profit
                profit = prices[R] - prices[L]
                max_profit = max(max_profit, profit)
            else:
                L = R
            R += 1
        return max_profit
            