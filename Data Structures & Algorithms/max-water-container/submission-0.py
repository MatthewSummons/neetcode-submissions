class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = -1
        i, j = 0, len(heights) - 1
        while i < j:
            curr_area = (j - i) * min(heights[i], heights[j]) 
            # print(curr_area)
            if curr_area >= max_area:
                max_area = curr_area
            
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return max_area


        