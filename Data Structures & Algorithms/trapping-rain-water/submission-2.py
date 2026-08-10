class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r, = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        max_area = 0
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                max_area += maxL - height[l] # will always be >= 0 because of maxL being at least = to height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                max_area += maxR- height[r]

        return max_area