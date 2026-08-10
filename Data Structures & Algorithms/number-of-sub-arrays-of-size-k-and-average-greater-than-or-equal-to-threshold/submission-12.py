class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        R = 0
        count = 0
        curSum = 0
        threshold *= k
        while R < len(arr):
            curSum += arr[R]
            # if r > window_size, then just keep adjusting
            if R >= k - 1:
                count += curSum >= threshold
                curSum -= arr[R - k + 1]
            
            R += 1
        
        return count


