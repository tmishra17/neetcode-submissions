class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count_sub_arr = 0
        for L in range(len(arr) - k + 1):
            #  sum starts at arr[L]
            sum_arr = arr[L]
            # why do we need to do L + k + 1 again?
            for R in range(L + 1, L + k):
                sum_arr += arr[R]
            
            # divide by number of subelements in array (k)
            avg = sum_arr // k
            print(avg)
            if avg >= threshold:
                count_sub_arr += 1
        
        return count_sub_arr
