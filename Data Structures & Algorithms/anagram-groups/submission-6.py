class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        res = []
        for word in strs:
            s_list = sorted(word)
            sorted_word = ''.join(s_list)
            hmap[sorted_word].append(word)
        
        for key in hmap.keys():
            res.append(hmap[key])

        return res