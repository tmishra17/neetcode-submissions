class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        pre = 1
        # 1 1 2 8 
        # pre: 8
        for i in range(0, len(nums)):
            res[i] *= pre
            pre *= nums[i]

        post = 1
        # 1 24 12 8 
        # post: 24
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        
        return res
# prefix and postfix