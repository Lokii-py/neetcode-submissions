class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        result = [1] * nums_len
        
        right_tracker = 1
        for i, n in enumerate(nums):
            result[i] = right_tracker
            right_tracker *= n

        left_tracker= 1
        for i in reversed(range(nums_len)):
            result[i] *= left_tracker
            left_tracker *= nums[i]
        return result