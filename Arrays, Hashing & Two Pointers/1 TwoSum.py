#First draft
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    if nums[i]+nums[j]==target:
                        if i<j:
                            return [i,j]
                        else:
                            return [j,i]
# O(n^2)

# Better Solusion O(n)
# By storing list into a hashmap    
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        val_idx={} # Create hashmap 

        for i, num in enumerate(nums):
            if target-num in val_idx:
                return [i, val_idx[target-num]]
            val_idx[num] = i
