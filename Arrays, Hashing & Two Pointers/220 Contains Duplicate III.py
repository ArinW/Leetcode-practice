# 1. [-2,5],2,5过不去因为i层直接没跑跳过到return False了因为range(0)
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        for i in range(len(nums)-indexDiff):
            for j in range(i+1,min(len(nums),i+1+indexDiff)):
                if abs(nums[j]-nums[i])<=valueDiff:
                    return True
        return False
    
#2. 太久了
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,min(len(nums),i+1+indexDiff)):
                if abs(nums[j]-nums[i])<=valueDiff:
                    return True
        return False
    
# 现根据value范围将数字分组存入hashmap，然后删除超出index范围的数字
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        bucket={}
        w=valueDiff+1

        for i, num in enumerate(nums):
            n=num//w
            if n in bucket:
                return True
            if n-1 in bucket and num-bucket[n-1]<=valueDiff:
                return True
            if n+1 in bucket and bucket[n+1]-num<=valueDiff:
                return True
            bucket[n]=num
            if i>=indexDiff:
                del bucket[num[i-indexDiff]//w]
            
        return False