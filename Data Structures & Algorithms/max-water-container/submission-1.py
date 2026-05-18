class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest_area = 0
        left_pointer = 0
        right_pointer = len(heights) - 1
        while left_pointer < right_pointer:
            height = min(heights[left_pointer], heights[right_pointer])
            width = right_pointer - left_pointer
            area = height * width
            if heights[right_pointer] < heights[left_pointer]:
                right_pointer -= 1
            elif heights[right_pointer] > heights[left_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
                left_pointer += 1
            largest_area = max(area, largest_area)
        return largest_area