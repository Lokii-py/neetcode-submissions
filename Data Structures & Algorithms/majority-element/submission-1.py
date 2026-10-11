class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        return max(hash_map, key=hash_map.get)