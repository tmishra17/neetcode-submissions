class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        window = set()
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                diff = prices[j] - prices[i]
                if diff > max_profit:
                    max_profit = diff
        
        return max_profit