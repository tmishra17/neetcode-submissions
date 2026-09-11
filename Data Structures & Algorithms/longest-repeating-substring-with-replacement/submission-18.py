class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        window = set()
        res = 0

        for r in range(len(s)):
            # increment the count each time, depending on which char it is
            count[s[r]] = 1 + count.get(s[r], 0)
            # get max value from the count dictionary
            max_count = max(count.values())
            # while window_size - max_count of letters in string so far is greater than k, that means that the number of replacements needed to make the string one consistent string is too long, switch it to a lower amount 
            while (r - l + 1) - max_count > k:
                # decrease the number that is inside of the list as that is typically the one that needs to be fixed the most
                count[s[l]] -= 1
                # decrease the window size until we have enough room for the replacements ((r - l + 1) - max_value <= 2)) replacements
                l += 1
            
            res = max(r - l + 1, res)

        return res