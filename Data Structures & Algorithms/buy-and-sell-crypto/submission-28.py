class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # set L and R = to 0 and 1
        L, R = 0, 1
        max_profit = 0

        while R < len(prices):
            # when profit is detected, evaluate profit and compare to max profit
            if prices[R] > prices[L]:
                profit = prices[R] - prices[L]
                max_profit = max(max_profit, profit)
            else:
                # not sure about this line, why not just L += 1?
                L = R
            R += 1

        return max_profit