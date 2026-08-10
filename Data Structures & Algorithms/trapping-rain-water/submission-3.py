class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        l, r = 0, len(height) - 1
        total_water = 0
        maxL, maxR = height[l], height[r]
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                total_water += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                total_water += maxR - height[r]
        return total_water