class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # int function with no parameters returns 0 by default
        hmap = defaultdict(int)
        res = []
        for num in nums:
            hmap[num] += 1
        
        sorted_map = dict(sorted(hmap.items(), key = lambda item: item[1], reverse=True))
        i = 0
        for key in sorted_map.keys():
            if i == k:
                break
            res.append(key)
            i += 1
        return res
            