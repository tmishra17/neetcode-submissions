class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        length = 0
        L = 0
        total = 0
        length = float("inf")
        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                length = min(R - L + 1, length)
                total -= nums[L]
                L += 1
            # compute min subarray by comparing R - L + 1 (new subarray)
            # and length (current min)
        
        return 0 if length == float("inf") else length