class Solution:
    def isValid(self, s: str) -> bool:
        opposite = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in opposite.keys() and stack:
                if opposite[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False