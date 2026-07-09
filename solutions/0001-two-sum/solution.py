class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem=0
        for i,num in enumerate(nums):
            rem=target-num
            if rem in nums:
               j= nums.index(rem)
               if i!=j:
                    return [i,j]
        
