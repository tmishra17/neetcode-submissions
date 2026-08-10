class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro = 0
        l, r = 0, 1
        while l < r and r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_pro = max(max_pro, profit)
            else:
                l = r
            # r is going through each day inside of the loop
            r += 1
            

        return max_pro