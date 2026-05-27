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
            else:
                if len(stack) > 0 and bracket_map[sign] == stack[-1]:
                    stack.pop()
                else:
                    return False
            print(stack)
        return len(stack) == 0