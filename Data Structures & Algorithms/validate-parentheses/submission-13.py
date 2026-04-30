class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '{' or c == '(' or c == '[':
                stack.append(c)
            elif stack:
                top = stack.pop()
                if top == '{' and c != '}':
                    return False
                elif top == '(' and c != ')':
                    return False
                elif top == '[' and c != ']':
                    return False
            elif not stack and c != '{' or c != '(' or c != '[':
                return False


        if stack:
            return False
        
        return True