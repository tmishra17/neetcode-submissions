class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0
        window.add(nums[L])

        R = L + 1
        while R < len(nums):
            # W  R
            # 1, 0? NO
            # 0, 1
            if abs(L - R) > k:
                window.discard(nums[L])
                L += 1
            if nums[R] in window:
                return True
            else:
                window.add(nums[R])
            R += 1

        return False