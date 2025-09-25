# 1. total没有在while中更新
def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        result=nums[0]+nums[1]+nums[2]
        diff= abs(result-target)
        for i in range(n-2):
            left, right = i+1, n-1
            total = nums[i] +nums[left]+nums[right]
            while left<right:
                if abs(total-target)<diff:
                    diff=abs(total-target)
                    result=total
                else:
                    if total>target:
                        right-=1
                    else:
                        left+=1
        return result
                
# 2.
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        result=nums[0]+nums[1]+nums[2]
        diff= abs(result-target)
        for i in range(n-2):
            left, right = i+1, n-1
            
            while left<right:
                total = nums[i] +nums[left]+nums[right]
                if abs(total-target)<diff:
                    diff=abs(total-target)
                    result=total
                else:
                    if total>target:
                        right-=1
                    else:
                        left+=1
        return result
                


