class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merging the nums1
        sorted_merged_list: List[int] = [0] * (len(nums1) + len(nums2))
        p_num1: int = 0
        p_num2: int = 0
        p_merging: int = 0

        while p_num1 < len(nums1) and p_num2 < len(nums2):
            if nums1[p_num1] >= nums2[p_num2]:
                sorted_merged_list[p_merging] = nums2[p_num2]
                p_num2 += 1
            else:
                sorted_merged_list[p_merging] = nums1[p_num1]
                p_num1 += 1
            p_merging += 1
        
        while p_num1 < len(nums1): 
            sorted_merged_list[p_merging] = nums1[p_num1]
            p_merging += 1
            p_num1 += 1

        while p_num2 < len(nums2):
            sorted_merged_list[p_merging] = nums2[p_num2]
            p_merging += 1
            p_num2 += 1

        if len(sorted_merged_list) % 2 != 0:
            med_idx: int = (len(sorted_merged_list) - 1) // 2
            return float(sorted_merged_list[med_idx])
        else:
            idx1: int = len(sorted_merged_list) // 2
            median: float = (sorted_merged_list[idx1] + sorted_merged_list[idx1-1]) / 2
            return median