class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        L, R = 0, 1
        h_set = set()
        count = 0
        h_set.add(s[L])
        max_len = 1
        while R < len(s):
            while s[R] in h_set and h_set:
                h_set.discard(s[L])
                L += 1
            
            h_set.add(s[R])
            max_len = max(max_len, len(h_set))
            R += 1
        
        return max_len
        