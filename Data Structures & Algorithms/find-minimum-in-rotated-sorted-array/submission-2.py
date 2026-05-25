class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums) - 1
        left = 0
        while left < right:
            mid_idx = (left+right) // 2
            if nums[mid_idx] < nums[right]:
                right = mid_idx
            else:
                left = mid_idx + 1
        return nums[right]
