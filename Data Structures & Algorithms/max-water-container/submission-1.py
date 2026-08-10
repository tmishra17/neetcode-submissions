class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #width abs(i - j)
        maxArea = 0
        for i in range(len(heights)):
            area = 0
            for j in range(i + 1, len(heights)):
                width = i - j
                area = (min(heights[i], heights[j])) * abs((i - j))
                maxArea = max(area, maxArea)
            
        return maxArea