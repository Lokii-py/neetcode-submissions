class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for sign in s:
            if sign in bracket_map.keys():
                if len(stack) > 0 and stack[-1] == bracket_map.get(sign, ''):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(sign)
        return len(stack) == 0