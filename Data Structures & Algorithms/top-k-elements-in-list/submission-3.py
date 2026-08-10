class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        freq = [[] for i in range(len(nums) + 1)] 
        ans = []
        for n in nums:
            count_dict[n] = 1 + count_dict.get(n, 0) # if n not in map, default value is 0
            
        for key, val in count_dict.items():
            freq[val].append(key)
        
        for i in range(len(freq) - 1, 0, -1):
            for item in freq[i]:
                print(item)
                if item not in ans:
                    ans.append(item)

                if len(ans) == k:
                    return ans