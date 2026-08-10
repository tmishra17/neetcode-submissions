class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h_set = set()
        L = 0 
        h_set.add(nums[L])
        for R in range(1, len(nums)):
            if R - L > k:
                h_set.remove(nums[L])
                L += 1
            # found duplicate
            if nums[R] in h_set:
                return True  
            h_set.add(nums[R])
        return False