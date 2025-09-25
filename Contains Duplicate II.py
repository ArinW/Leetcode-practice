class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_hash = {}
        for i, num in enumerate(nums):
            if num in nums_hash:
                if i-nums_hash[num] <= k:
                    return True
            nums_hash[num]=i
        return False