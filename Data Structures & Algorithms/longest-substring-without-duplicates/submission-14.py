class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        h_set = set()
        max_len = 0
        
        for R in range(len(s)):
            # shift L until we reach s[R]
            while s[R] in h_set:
                h_set.discard(s[L])
                L += 1
            
            h_set.add(s[R])
            max_len = max(max_len, len(h_set))
            R += 1
        
        return max_len
        