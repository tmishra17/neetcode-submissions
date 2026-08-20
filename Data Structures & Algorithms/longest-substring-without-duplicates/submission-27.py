class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        # start l at 0 and r will increase
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp: # if new value inside of the map, move l past index at mp[s[r]] to get past duplicate)
            # move l past duplicate r to avoid a bad result
                l = max(mp[s[r]] + 1, l)
            # new s[r] index shows new r index
            mp[s[r]] = r

            res = max(res, r - l + 1) # max_res between prev max window size and current window size
        return res
