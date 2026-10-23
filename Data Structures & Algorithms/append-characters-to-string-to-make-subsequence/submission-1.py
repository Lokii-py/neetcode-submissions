class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        while i <= (len(s) - 1) and j <= (len(t) - 1):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return len(t) - j 