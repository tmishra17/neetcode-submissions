class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # TC: O(n) - n is the number of characters in s
        # SC: O(k) - k is the size of the window
        L = 0 # Left pointer, remove leftmost values from window until duplicate value is removed and then you find 
        max_len = 0 # length of longest substring
        window = set() # window that will contain all unique substrings
        for R in range(len(s)):
            while s[R] in window: # if s[R] still inside of the window, remove values until it is completely gone
                window.discard(s[L]) # discard s[L] from the window until the duplicate is gone
                L += 1 # check for the next L value
            
            window.add(s[R]) # if it is not in the window, add s[R] and then compare to max_len and assign the highest value
            max_len = max(max_len, len(window)) # compare max_len and window length and determine which one is bigger.
        return max_len