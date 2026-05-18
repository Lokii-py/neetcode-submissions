class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        left_product = [1 for i in range(nums_len)]
        right_product = [1 for i in range(nums_len)]

        i = 1
        j = nums_len - 2 
        while (i < nums_len) and (j >= 0):
            left_product[i] = left_product[i-1] * nums[i - 1]
            i += 1

        # j = nums_len - 2 
        # while (i >= 0):
            right_product[j] = right_product[j+1] * nums[j+1]
            j -= 1
        
        result = [a * b for a, b in zip(right_product, left_product)]
        return result