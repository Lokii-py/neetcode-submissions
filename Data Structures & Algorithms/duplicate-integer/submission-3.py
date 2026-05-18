class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # num = set(nums)
        # if len(num) != len(nums):
        #     return True
        # return False

        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)

        return False