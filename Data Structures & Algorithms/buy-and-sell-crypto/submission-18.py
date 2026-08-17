class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # start max_profit at 0
        max_profit = 0

        # for each number in the list - calculate the current profit and compare it to the max_profit
        for i in range(len(prices)):
            # start at i + 1 because you wouldn't sell on the same day, there would be no profit
            for j in range(i + 1, len(prices)):
                # calculate profit and compare its value to max_profit
                # subtract the current price i to the price of the future stock j to determine if the profit is bigger than max profit, then compare profit and max profit
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
# TC: O(n*(n - i)) where 0 < i <= n
# SC: O(1) no memory used
        return max_profit