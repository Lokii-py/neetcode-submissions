class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1
            
        required = len(need)
        have = 0

        wind_dict = {}
        left_pointer = 0
        min_length = float('inf')
        min_start_window = 0

        for right_pointer, char in enumerate(s):
            wind_dict[char] = wind_dict.get(char, 0) + 1
            
            if char in need and wind_dict[char] == need[char]:
                have += 1
                
            while have == required:
                current_window_length = right_pointer - left_pointer + 1
                if current_window_length < min_length:
                    min_length = current_window_length
                    min_start_window = left_pointer
                
                left_char = s[left_pointer]
                wind_dict[left_char] -= 1
                
                if left_char in need and wind_dict[left_char] < need[left_char]:
                    have -= 1
                
                left_pointer += 1
                
        if min_length == float('inf'):
            return ""
            
        return s[min_start_window : min_start_window + min_length]