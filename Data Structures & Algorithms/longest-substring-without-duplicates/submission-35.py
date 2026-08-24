class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hmap implementation
        mp = {}
        max_len = L = 0
        for R in range(len(s)):
            if s[R] in mp:
                L = max(mp[s[R]] + 1, L) # if R is inside of the map, move L to the right
            mp[s[R]] = R # here we are just adding values to the map.
            max_len = max(max_len, R - L + 1)
        # return the maximum length of the substr in the end
        # TC: O(n) for number of items inside of the list
        # SC: O(k) for the size of the window
        return max_len