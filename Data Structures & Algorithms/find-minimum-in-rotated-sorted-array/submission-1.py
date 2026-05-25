class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = float('inf')
        for num in nums:
            min_val = min(min_val, num)
        return min_val