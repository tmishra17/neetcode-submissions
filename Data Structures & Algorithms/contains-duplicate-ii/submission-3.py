class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
     
        # we do l + k because we want to make sure that the window moves with each iteration
        for l in range(len(nums)):
            # detect whether you are allowed to have a full window
            for r in range(l + 1, min(len(nums), l + k + 1)):
                if nums[l] == nums[r]:
                    # Has Duplicate
                    return True
        return False
           