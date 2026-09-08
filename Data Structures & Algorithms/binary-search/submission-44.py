class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # iterative binary search
        l, r = 0, len(nums) - 1
        while l <= r:
            # prevents overflow as l and r could add up to really big number with just normal average
            m = l + (r - l) // 2
            # nums too small, so cut off left half of the array
            if nums[m] < target:
                l = m + 1
            # nums too big, so cut off right half of the array
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        # target not found in list so return -1
        return -1