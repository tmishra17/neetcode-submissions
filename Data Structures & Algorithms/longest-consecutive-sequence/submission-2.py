class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_sequence = 0
        store = set(nums)
        for num in nums:
            count, curr = 0, num
            while curr in store:
                count += 1
                curr += 1
            
            max_sequence = max(count, max_sequence)
        
        return max_sequence
        # hs = {}
        # max_sequence = 0
        # i = 0
        # while i < len(nums):
        #     count = 0
        #     hs.add(nums[i])
        #     if nums[i] - 1 not in hs:
        #         while abs(nums[i] - nums[i + 1]) == 1:
        #             count += 1
        #             i += 1
        #     max_sequence = max(max_sequence, count)
        # return max_sequence
        