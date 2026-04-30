class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for c in tokens:
            if c != '+' and c != '-' and c != '*' and c != '/':
                numStack.append(int(c))
            else:
                num2 = numStack.pop()
                num1 = numStack.pop()
                if c == '+':
                    numStack.append(num1 + num2)
                elif c == '-':
                    numStack.append(num1-num2)
                elif c == '*':
                    numStack.append(num1 * num2)
                elif c == '/':
                    numStack.append(int(num1 / num2))
        return numStack.pop()


