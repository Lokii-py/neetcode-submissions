class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        len_substring = 0
        for char in s:
            if len(substring) > 0:
                if substring[0] == char:
                    substring.replace(char, "")
                elif char in substring:
                    substring = ""
            if char not in substring:
                substring += char
            len_substring = max(len_substring, len(substring))
        return len_substring