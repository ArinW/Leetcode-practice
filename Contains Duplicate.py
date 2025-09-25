#1. 如果list太长就很麻烦
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        val=[]
        for i, num in enumerate(nums):
            if num in val:
                return True
            val.append(num)
        return False

# 2. sort and compare to next one
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True

        return False
    
#3. 和1方法思路是一样的，只是使用了set， 比2快 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for n in nums:
            if n in num_set:
                return True
            num_set.add(n)
        return False
    
#4.把3换成hash，会慢一些
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_hash = {}
        for n in nums:
            if n in num_hash:
                return True
            num_hash[n]= -1
        return False
    
#5.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(set(nums))<len(nums) else False    