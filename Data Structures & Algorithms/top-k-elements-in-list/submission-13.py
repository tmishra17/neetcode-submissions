class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # int function with no parameters returns 0 by default
        hmap = defaultdict(int)
        res = []
        count = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            hmap[num] += 1
        print(hmap.keys())
        for key, val in hmap.items():
            count[val].append(key)
                
        for i in range(len(count) - 1, 0, -1):
            if count[i]:
                for num in count[i]:
                    res.append(num)
                    k -= 1
            if k == 0:
                break
                

        return res
            