class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visted={}
        for i in range (len(nums)):
            visted[nums[i]]=i
        for i in range(len(nums)):
            rem=target-nums[i]
            if rem in visted and i != visted[rem]:
                return[visted[rem],i]
