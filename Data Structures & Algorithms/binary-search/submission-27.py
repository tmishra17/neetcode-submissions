class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)

    def binary_search(self, nums: List[int], l: int, h: int, target: int) -> int:
        if l > h: # means we have covered all of the items in the list and target was not found, if we don't have this, we won't know when to stop
            return -1 
        mid = (l + h) // 2 # middle or average of low + high
        # first check if the mid is within the range of the list, if not then the list size is too small or target is not inside of the list
        if mid < 0 or mid > len(nums) - 1:
            return -1 # target not found in the list
        
        if nums[mid] < target:
            # call function on the upper half of the sorted list, adjust L to + 1 the mid and search withi that window
            return self.binary_search(nums, mid + 1, h, target)
        elif nums[mid] > target:
            # call function of the lower half since mid is too big, so high becomes mid - 1 b/c mid to n is too big for target, the goal is to match the mid indice with the target
            return self.binary_search(nums, l, mid - 1, target)
        else:
            # this means we have found target inside of the list, so return the indice
            return mid # mid is what we match with the target in binary search
        
