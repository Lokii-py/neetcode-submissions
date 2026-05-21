class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left_pointer = 0
        max_len = 0
        count_dict = {}
        for right_pointer, char in enumerate(s):
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
            while (right_pointer-left_pointer + 1) - max(count_dict.values()) > k:
                count_dict[s[left_pointer]] -= 1
                left_pointer += 1

            max_len = max(max_len, right_pointer-left_pointer + 1)
        return max_len