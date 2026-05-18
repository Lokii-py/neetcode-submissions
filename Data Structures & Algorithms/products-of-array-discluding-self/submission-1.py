class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        left_product = [1 for i in range(nums_len)]
        right_product = [1 for i in range(nums_len)]

        i = 0
        while i < nums_len:
            right_product[i] = math.prod(nums[i+1:nums_len])
            left_product[i] = math.prod(nums[0:i])
            i += 1
        
        result = [a * b for a, b in zip(right_product, left_product)]
        return result