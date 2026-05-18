class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tag = []

        for i in range(len(nums)): 
            x = target - nums[i]
            if x in nums[i+1:]:
                tag.append(i)
                tag.append(nums[i+1:].index(x) + (i + 1))
                return tag

        return []
        