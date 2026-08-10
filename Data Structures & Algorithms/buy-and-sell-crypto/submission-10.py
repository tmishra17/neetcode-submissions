class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        # find values where prices[l] < prices[r]
        # need to also make sure that r does not go over the list
        while r < len(prices):
            
            if prices[l] > prices[r]:
                # find prices where prices[l] < prices[r]
                l = r 
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
                r += 1
       
        return max_profit  