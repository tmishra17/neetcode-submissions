class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        # we do l + k because we want to make sure that the window moves with each iteration
        l = 0
        for r in range(len(nums)):
            # detect whether you are allowed to have a full window
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False
           