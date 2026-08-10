class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_sequence = 0
        nums_set = set(nums)
        for num in nums_set:
            temp_num = num
            sequence = 0
            if temp_num - 1 not in nums_set: # start of a sequence
                
                while temp_num in nums_set:
                    temp_num += 1
                    sequence += 1
            
            if sequence > max_sequence:
                max_sequence = sequence 

        return max_sequence


