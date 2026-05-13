class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens: 
            match x: 
                case "+":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(l + r)
                case "-":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(l - r)
                case "*":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(l * r)
                case "/":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(int(l / r))
                case x:
                    stack.append(int(x))
        if stack:
                return stack[-1]
        