# 1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums_s = sorted(nums)
        nums_r = sorted(nums,reverse=True)

        for i in range(len(nums_s)):
            for j in range(len(nums_r)):
                if nums_s[i]<=0 and i<j:
                    if nums_s[i]+nums_s[j]<=0:
                        if nums_s[i]+nums_r[j]+nums_r[j+1]==0: #容易out of range
                            result.append([nums_s[i], nums_r[j], nums_r[j+1]])
                    else:
                        if nums_s[i]+nums_r[j]+nums_s[i+1]==0 :
                            result.append([nums_s[i], nums_r[j], nums_s[i+1]])
        return result

# Two pointer
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n=len(nums)

        for i in range(n-2):
            left, right = i+1, n-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while left<right:
                total = nums[i]+nums[left]+nums[right]
                if total == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1


        return result
