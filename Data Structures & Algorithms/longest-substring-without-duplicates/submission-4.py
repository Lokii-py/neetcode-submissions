class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_pointer = 0
        seen_char = {}
        len_substring = 0
        for idx, char in enumerate(s):
            if char in seen_char:
                left_pointer = max(left_pointer, seen_char[char] + 1)
            seen_char[char] = idx
            len_substring = max(len_substring, idx - left_pointer + 1)
        return len_substring

