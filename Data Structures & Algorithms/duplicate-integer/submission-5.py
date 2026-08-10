class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hMap = {}
        for num in nums:
            if num not in hMap:
                hMap[num] = num
            else:
                return True
        return False
