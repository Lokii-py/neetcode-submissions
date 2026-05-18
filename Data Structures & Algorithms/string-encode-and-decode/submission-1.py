class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list = []
        for word in strs:
            encoded_list.append(str(len(word)))
            encoded_list.append('#')
            encoded_list.append(word)
        encoded_str = "".join(encoded_list)
        return encoded_str
        
    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0

        while i < len(s):
            j = s.find('#', i)
            
            intermediate_num = s[i:j]
            length = int(intermediate_num)

            start_idx = j + 1
            end_idx = start_idx + length
            word = s[start_idx:end_idx]
            decoded_str.append(word)
            i = end_idx
        return decoded_str