class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for sign in s:
            if sign in bracket_map.values():
                stack.append(sign)
            if sign in bracket_map.keys():
                if len(stack) > 0 and stack[-1] == bracket_map.get(sign, ''):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0