class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # move over the L pointer by 1 once we find a duplicate
        
        max_len = 0 # maximum length of longest non dupe substring
        L = R = 0 # start window size at 1 
        window = set() # window we are using to keep track of the values, need this to remember if we have already seen this number before
        # what if the farthest left value in the window is not the duplicate, remove from the set
        for R in range(len(s)):
            while s[R] in window:
                window.discard(s[L])
                L += 1
            # R outside length of the window on the next iteration
            window.add(s[R]) # add s[R] once duplicates are gone and then compute the max window size
            max_len = max(max_len, len(window)) # calculate max_len if str_len bigger, put it outside incase we never find another duplicate

        return max_len # return the actual max_len once done with the problem
# TC: O(n) where n is the size of the array
# SC: O(k) where k is the size of the window and 0 <= k <= n