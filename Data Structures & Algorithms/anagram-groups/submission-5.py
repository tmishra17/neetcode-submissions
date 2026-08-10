class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hmap = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            # must be an immutable key
            hmap[tuple(count)].append(word)

        for key in hmap.keys():
            res.append(hmap[key])
        
        return res