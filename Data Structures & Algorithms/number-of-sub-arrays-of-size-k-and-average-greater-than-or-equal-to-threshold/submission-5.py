class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count_sums = 0
        curSum = sum(arr[:k])
        minSum = k * threshold
        
        if curSum >= minSum:
            count_sums += 1
        
        for R in range(k, len(arr)):
            L = R - k
            curSum = curSum + arr[R] - arr[L]
            
            if curSum >= minSum:
                count_sums += 1

        return count_sums