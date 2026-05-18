class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        sorted_nums = sorted(list(set(nums)))
        max_len = 1
        current_len = 1
        i = 0
        while i < (len(sorted_nums)-1):
            if sorted_nums[i+1] - sorted_nums[i] == 1:
                current_len += 1
            else:
                current_len = 1
            max_len = max(max_len, current_len)
            i += 1
        return max_len