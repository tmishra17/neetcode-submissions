class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Loop
        L, R = 0, len(nums) - 1 # start L&R at beginning and end to signify the edges of the list
        while L <= R:
            mid = L + ((R - L) // 2) # to get the mid point, compute the average between the two L and R points
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                L = mid + 1
            else:
                R = mid - 1 # cut the array size less than mid to cut it in half
        return -1