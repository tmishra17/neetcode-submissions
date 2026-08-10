class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count_sub_arr = 0
        # get first sliding window sum
        curSum = sum(arr[:k])
        minSum = k * threshold
        if curSum >= minSum:
            count_sub_arr = 1
        
        for R in range(k, len(arr)):
            L = R - k

            curSum = curSum + arr[R] - arr[L]

            if curSum >= minSum:
                count_sub_arr += 1
        return count_sub_arr
