class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # iterate through each value in the array
        for R in range(len(nums)):
            # compare each value of L with R to see if there are any duplicates
            # also make sure it does not go over the limit of the array size
            for L in range(R + 1, min(len(nums), R + k + 1 )):
                # if there is a duplicate within our window
                if nums[L] == nums[R]:
                    return True

        return False
