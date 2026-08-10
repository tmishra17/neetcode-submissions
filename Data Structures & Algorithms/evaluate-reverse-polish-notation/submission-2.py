class Solution:
    def isOperand(self, n):
        return n == '+' or n == '-' or n == '*' or n == '/'

    def evalOperand(self, n, lhs, rhs):
        print(lhs, n ,rhs)
        if n == '+':
            return lhs + rhs
        elif n == '-':
            return lhs - rhs
        elif n == '/':
            return lhs / rhs
        elif n == '*':
            return lhs * rhs
            
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if self.isOperand(n):
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(self.evalOperand(n, int(lhs), int(rhs)))
                print(stack[-1])
            else: 
                #print(n)
                stack.append(n)

        return int(stack[-1])
    
    