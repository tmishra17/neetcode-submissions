class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {')' : '(', '}' : '{', ']' : '['} 
        stack = []
        for c in s:
            if c not in hmap: # if open parentheses, append to stack
                stack.append(c)
                continue
            if not stack or stack[-1] != hmap[c]: # then check if corresponding close parentheses is with open parentheses
                return False
            stack.pop()
            
        return not stack