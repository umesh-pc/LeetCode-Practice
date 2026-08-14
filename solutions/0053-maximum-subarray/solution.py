class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best=nums[0]
        max_sum=nums[0]
        for i in range(1,len(nums)):
            max_sum=max(nums[i],max_sum+nums[i])
            best=max(best,max_sum)
        return best 



