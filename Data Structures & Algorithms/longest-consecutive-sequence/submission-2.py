class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        sorted_nums = sorted(nums)
        pattern_lens = []
        pattern_len = 0
        i = 0
        while i < (len(sorted_nums)-1):
            num = sorted_nums[i+1] - sorted_nums[i]
            if abs(num) == 1:
                pattern_len += 1  
            elif num == 0:
                pattern_len += 0
            else:
                pattern_lens.append(pattern_len)
                pattern_len = 0
            pattern_lens.append(pattern_len)
            i += 1

        val = max(pattern_lens) + 1
        return val