class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in {"+", "-", "*", "/"}:
                print(c)
                stack.append(int(c))
            else:
                # LIFO
                num2 = stack.pop() # right
                print("right:", num2)
                num1 = stack.pop() # left 
                print("left:", num1)
                if c == "+":
                    stack.append(num1+num2)
                elif c == "-":
                    stack.append(num1-num2)
                elif c == "*":
                    stack.append(num1*num2)
                else:
                    stack.append(int(num1 / num2))
        return stack[0]