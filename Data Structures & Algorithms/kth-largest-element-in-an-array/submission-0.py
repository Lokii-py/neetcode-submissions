import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target: int = len(nums) - k
        lo = 0
        hi = len(nums)-1

        while True:
            p_idx = partition(nums, lo, hi)
            if p_idx == target:
                return nums[p_idx]
                break
            elif target < p_idx:
                hi = p_idx - 1
            else:
                lo = p_idx + 1


def partition(nums: List[int], lo: int, hi: int):
    rand_pivot = random.randint(lo, hi)
    nums[lo], nums[rand_pivot] = nums[rand_pivot], nums[lo]

    p: int = lo
    i: int = lo+1
    j: int = hi

    while True: 
        while i < hi and nums[p] > nums[i]:
            i += 1

        while j > lo and nums[p] < nums[j]:
            j -= 1

        if i >= j:
            break

        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    
    nums[p], nums[j] = nums[j], nums[p]
    return j
