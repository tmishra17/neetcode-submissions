class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        h_map = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            h_map[tuple(count)].append(word)
        
        return list(h_map.values())
            
