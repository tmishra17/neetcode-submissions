class Solution:
    def findMin(self, nums: List[int]) -> int:
        # left child
        min_v = nums[0]
        for i in range(len(nums)):
            min_v = min(min_v, nums[i])

        return min_v