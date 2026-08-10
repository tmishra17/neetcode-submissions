class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {} 
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hMap:
                return [hMap[difference], i]
            hMap[nums[i]] = i

        return -1