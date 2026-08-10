class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for c in s:

            if c.isalnum():
                temp += c.lower()
        print(temp)
        return temp == temp[::-1]