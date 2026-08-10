class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        i = 0
        max_seq = 0
        for num in nums:
            # start of a sequence
            if num - 1 not in nums:
                count = 0
                # if it is in the set, increase count by one
                while num + count in num_set:
                    count += 1

                max_seq = max(max_seq, count)
        
        return max_seq
