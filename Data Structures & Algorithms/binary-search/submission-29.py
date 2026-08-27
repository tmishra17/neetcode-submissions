class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # TC: O(log n) for each sub array inside of the list
        # SC: O(log n) for each recursive call on the stack
        return self.binary_search(nums, 0, len(nums) - 1, target)

    def binary_search(self, nums: List[int], l: int, r: int, target: int) -> int:
        # check if l > r, if so then that means that target was not found in the list, so return -1
        if l > r:
            return -1
        
        # otherwise check if nums[mid] > target, if so the right half is too big so change range to L -- (mid - 1), if mid is smaller than target, then move L past the mid point, changing the range to m + 1 -- R, if nums[m] == to target, return m because that is the location of target in the list
        m = (l + r) // 2 # integer division to prevent decimals
        if nums[m] < target:
            # l = m + 1, for the right sub array
            return self.binary_search(nums, m + 1, r, target)
        elif nums[m] > target:
            # r = m - 1, for the left sub array
            return self.binary_search(nums, l, m - 1, target)
        else:
            # target found in the list, so return locatoin
            return m
        