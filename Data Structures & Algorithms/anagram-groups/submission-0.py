class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Check if the strs is empty or not 
        # Also, check if the there is only one string inside list
        # If yes, return the strs
        if not strs or (len(strs) == 1):
            return [strs]
        
        hashmap = {}
        for word in strs:
            transformed_word = sorted(word)
            transformed_word = "".join(transformed_word)
            if transformed_word not in hashmap:
                hashmap[transformed_word] = [word]
            else :
                hashmap[transformed_word].append(word)
        
        output = []
        for j, k in hashmap.items():
            output.append(k)
        return output
    