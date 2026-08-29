class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find the min, by finding if the left or subsection is smaller than the mid subsection
        # if the left is smaller, r= mid -1, if the right is smaller, l = mid + 1
        # if the mid is the smallest, l = mid - 1 and r = mid + 1 and then return the min between the two values
        L, R = 0, len(nums) - 1

        while L < R:
            # Prevent overflow from too big numbers
            mid = L + ((R - L) // 2)
            # smallest value is inside the right subsection
            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid
        
        return nums[L]