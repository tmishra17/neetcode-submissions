class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)

    def binary_search(self, l: int, r: int, nums: List[int], target:int) -> int:
        # meaning target was not found inside of the array
        if l > r:
            return -1
        # add l to offset to the location of where we want the binary search to occur, integer division to prevent decimals
        mid = l + (r - l) // 2
        # if nums[mid] < target, cut the left half of the array b/c it will not be in there
        if nums[mid] < target:
            #  mid + 1 b/c we know it is not at mid
            return self.binary_search(mid + 1, r, nums, target)
        # mid is larger than the target, so cut off the right half so we can focus on this subsection, mid - 1 because we know it is not mid
        elif nums[mid] > target:
            return self.binary_search(l, mid - 1, nums, target)
        # at this point, by definition, nums[mid] == target, so return mid
        else:
            return mid
