class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, total = 0,0
        length = float("inf")
        for R in range(len(nums)):
            total += nums[R]

            while total >= target:
                total -= nums[L] # substracting so that we keep some sum when we move onto the next one
                length = min(R - L + 1, length) # which is smaller, size of window, or length?, every time we decrement L we have to make sure that length is the smallest subarray
                L += 1
        
        return 0 if length == float("inf") else length