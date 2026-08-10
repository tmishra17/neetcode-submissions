class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        Map = {')': '(', '}': '{', ']' : '['}
        stack = []
        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            else:
                if not stack or stack[-1] != Map[c]:
                    return False
                stack.pop()

        return not stack 
            


    
                


                    

        