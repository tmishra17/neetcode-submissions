class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L = R = 0
        l_str = 0
        while R < len(s):
            while s[R] in window:
                # while s[R] still in the window remove vals until dupe is gone
                window.remove(s[L])
                # reset window size
                L += 1
            
            window.add(s[R])
            # max will always be window size
            l_str = max(l_str, R - L + 1)
            R += 1
        return l_str
            