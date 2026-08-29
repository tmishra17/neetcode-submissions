class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1 # start at the beginning and end of the list
        
        while l <= h:
            # calulate mid, if number at index mid < target, then move l to mid + 1 and focus on right subarray, nums[mid] > target means right subarray is too big so focus on; if number at mid equals target,
            # (l + h) // 2 can lead to overflow 
            mid = l + ((h - l) // 2)
            print(f"l: {l}, h: {h}, mid: {mid}, nums[mid]: {nums[mid]}")
            if nums[mid] < target:
                # for right subarray
                l = mid + 1
                print("worked")
            
            elif nums[mid] > target:
                # for left subarray
                h = mid - 1
            else:
                return mid
        print(f"l: {l}")
        return -1