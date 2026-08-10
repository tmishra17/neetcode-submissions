class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        for c in s:
            new_str = ""
            for i in range(len(s)):
                if s[i] != c:
                    new_str += s[i]
            
            if new_str == new_str[::-1]:
                return True
        
        return False