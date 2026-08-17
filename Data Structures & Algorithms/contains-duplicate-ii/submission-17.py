class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for L in range(len(nums)):
            # look at each combination of numbers to get to the i section
            for R in range(L + 1, min(len(nums), L + k + 1)):
                if nums[L] == nums[R]:
                    return True

# TC: O(n*min(n, k))
# SC: O(1)
        return False