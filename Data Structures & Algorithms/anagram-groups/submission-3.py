class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hmap = {}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            #  must be immutable to be a key
            count = tuple(count)
            if count in hmap:
                hmap[count].append(word)
            else:
                hmap[count] = [word]

        for key in hmap.keys():
            res.append(hmap[key])
        
        return res