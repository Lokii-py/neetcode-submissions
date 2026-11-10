class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        if not s:
            return True
        
        k = 0
        for i in range(len(t)):
            if k < len(s) and s[k] == t[i]:
                k += 1
            if k == len(s):
                return True
        return len(s) == k